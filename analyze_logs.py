import os
import re
from collections import defaultdict
from datetime import datetime
import argparse

def parse_timestamp(line):
    """Extract timestamp from log line."""
    match = re.match(r"\[(.*?)\]", line)
    if match:
        return datetime.strptime(match.group(1), "%Y-%m-%d %H:%M:%S,%f")
    return None

def parse_logical_clock(line):
    """Extract logical clock value from log line."""
    match = re.search(r"logical clock: (\d+)", line.lower())
    if match:
        return int(match.group(1))
    return None

def parse_queue_length(line):
    """Extract queue length from log line."""
    match = re.search(r"queue size: (\d+)", line.lower())
    if match:
        return int(match.group(1))
    return None

def analyze_experiment(exp_dir):
    """Analyze logs from a single experiment."""
    results = {
        "clock_jumps": defaultdict(list),
        "queue_lengths": defaultdict(list),
        "max_clock_values": {},
        "clock_drift": {},
        "avg_queue_length": {},
        "message_patterns": defaultdict(lambda: defaultdict(int)),
        "clock_rates": {},
        "time_based_drift": defaultdict(list),
        "queue_growth_rate": defaultdict(list)
    }
    
    # Analyze each machine's logs
    for i in range(3):
        log_file = f"{exp_dir}/machine_{i}.log"
        if not os.path.exists(log_file):
            continue
            
        prev_clock = None
        queue_lengths = []
        
        # Extract clock rate from first line
        with open(log_file, "r") as f:
            first_line = f.readline()
            rate_match = re.search(r"clock rate (\d+) ticks/second", first_line)
            if rate_match:
                results["clock_rates"][i] = int(rate_match.group(1))
        
        with open(log_file, "r") as f:
            lines = f.readlines()
        
        prev_time = None
        prev_queue_len = None
        
        for line in lines:
            timestamp = parse_timestamp(line)
            clock_val = parse_logical_clock(line)
            queue_len = parse_queue_length(line)
            
            # Analyze message patterns
            if "INTERNAL EVENT" in line:
                results["message_patterns"][i]["internal"] += 1
            elif "SENT" in line:
                if "all" in line.lower():
                    results["message_patterns"][i]["broadcast"] += 1
                else:
                    results["message_patterns"][i]["point-to-point"] += 1
            elif "RECEIVED" in line:
                results["message_patterns"][i]["received"] += 1
            
            # Analyze clock jumps and values
            if clock_val is not None:
                if prev_clock is not None:
                    jump = clock_val - prev_clock
                    if jump > 1:  # Record jumps larger than 1
                        results["clock_jumps"][i].append(jump)
                prev_clock = clock_val
                results["max_clock_values"][i] = clock_val
                
                # Track time-based drift
                if timestamp and prev_time:
                    time_diff = (timestamp - prev_time).total_seconds()
                    if time_diff > 0:
                        drift_rate = (clock_val - prev_clock) / time_diff
                        results["time_based_drift"][i].append(drift_rate)
                prev_time = timestamp
            
            # Analyze queue behavior
            if queue_len is not None:
                queue_lengths.append(queue_len)
                if prev_queue_len is not None and timestamp and prev_time:
                    time_diff = (timestamp - prev_time).total_seconds()
                    if time_diff > 0:
                        queue_growth = (queue_len - prev_queue_len) / time_diff
                        results["queue_growth_rate"][i].append(queue_growth)
                prev_queue_len = queue_len
        
        if queue_lengths:
            results["avg_queue_length"][i] = sum(queue_lengths) / len(queue_lengths)
            results["queue_lengths"][i] = queue_lengths
    
    # Calculate clock drift between machines
    for i in range(3):
        for j in range(i + 1, 3):
            if i in results["max_clock_values"] and j in results["max_clock_values"]:
                drift = abs(results["max_clock_values"][i] - results["max_clock_values"][j])
                results["clock_drift"][(i, j)] = drift
    
    return results

def main():
    """Analyze a single experiment run."""
    parser = argparse.ArgumentParser(description='Analyze logical clock experiment logs.')
    parser.add_argument('--config', type=str, choices=['default', 'modified'], required=True,
                      help='Configuration type (default or modified)')
    parser.add_argument('--run', type=int, required=True,
                      help='Run number to analyze')
    args = parser.parse_args()

    # Find the specific experiment directory
    experiments_dir = "experiments"
    exp_prefix = f"{args.config}_run_{args.run}"
    
    # Find the matching directory
    matching_dirs = []
    for dir_name in os.listdir(experiments_dir):
        if dir_name.startswith(exp_prefix):
            matching_dirs.append(dir_name)
    
    if not matching_dirs:
        print(f"No experiment found for {exp_prefix}")
        return
    
    # Use the most recent if multiple matches
    exp_dir = os.path.join(experiments_dir, sorted(matching_dirs)[-1])
    
    # Analyze the experiment
    results = analyze_experiment(exp_dir)
    
    # Generate observations
    observations = []
    
    # Add experiment info
    observations.append(f"# Logical Clock System Observations - {args.config.title()} Run {args.run}\n")
    observations.append(f"## Experiment Directory: {os.path.basename(exp_dir)}\n")
    
    # System characteristics
    observations.append("## System Characteristics")
    for vm_id, rate in sorted(results["clock_rates"].items()):
        observations.append(f"\nVM {vm_id}:")
        observations.append(f"- Clock rate: {rate} ticks/second")
    
    # Message patterns
    observations.append("\n## Message Patterns")
    for vm_id in sorted(results["message_patterns"].keys()):
        observations.append(f"\nVM {vm_id}:")
        total_msgs = sum(results["message_patterns"][vm_id].values())
        for msg_type, count in results["message_patterns"][vm_id].items():
            percentage = (count / total_msgs * 100) if total_msgs > 0 else 0
            observations.append(f"- {msg_type}: {percentage:.1f}% ({count} messages)")
    
    # Clock behavior
    observations.append("\n## Clock Behavior")
    for vm_id in sorted(results["clock_jumps"].keys()):
        jumps = results["clock_jumps"][vm_id]
        if jumps:
            avg_jump = sum(jumps) / len(jumps)
            max_jump = max(jumps)
            observations.append(f"\nVM {vm_id}:")
            observations.append(f"- Average jump size: {avg_jump:.2f}")
            observations.append(f"- Maximum jump size: {max_jump}")
            observations.append(f"- Number of jumps: {len(jumps)}")
            observations.append(f"- Final clock value: {results['max_clock_values'][vm_id]}")
    
    # Queue analysis
    observations.append("\n## Queue Behavior")
    for vm_id in sorted(results["queue_lengths"].keys()):
        lengths = results["queue_lengths"][vm_id]
        if lengths:
            avg_length = sum(lengths) / len(lengths)
            max_length = max(lengths)
            observations.append(f"\nVM {vm_id}:")
            observations.append(f"- Average queue length: {avg_length:.2f}")
            observations.append(f"- Maximum queue length: {max_length}")
            observations.append(f"- Queue length measurements: {len(lengths)}")
    
    # Clock drift
    observations.append("\n## Clock Drift")
    for (vm1, vm2), drift in sorted(results["clock_drift"].items()):
        observations.append(f"\nBetween VM {vm1} and VM {vm2}:")
        observations.append(f"- Final drift: {drift} ticks")
    
    # Write observations to file
    output_file = f"observations_{args.config}_run_{args.run}.md"
    with open(output_file, "w") as f:
        f.write("\n".join(observations))
    
    print(f"Analysis complete. Results written to {output_file}")

if __name__ == "__main__":
    main()
