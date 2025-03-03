# Logical Clocks in Distributed Systems

This project implements a model of a small, asynchronous distributed system with Lamport's Logical Clocks. The system consists of multiple virtual machines running at different speeds on a single physical machine, demonstrating the concepts of logical time and message passing in distributed systems.

## Features

- Multiple virtual machines running at different clock rates (1-6 ticks/second)
- Asynchronous message passing between machines
- Implementation of Lamport's Logical Clocks
- Event logging with system time and logical clock values
- Random event generation (internal events vs. message sending)

## Setup

1. Create and activate a virtual environment:
   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate on macOS/Linux
   source venv/bin/activate

   # Activate on Windows
   .\venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the simulation:
   ```bash
   python main.py
   ```

4. To deactivate the virtual environment when done:
   ```bash
   deactivate
   ```

## System Design

- Each virtual machine runs at a random clock rate between 1-6 ticks/second
- Machines communicate via TCP sockets
- Events are logged to individual log files in the `logs` directory
- On each clock cycle, machines either:
  - Process a message from their queue
  - Generate a random event (send message to one machine, all machines, or internal event)

## Log Files

Log files are created in the `logs` directory with the format `machine_<id>.log`. Each log entry includes:
- System time
- Event type (send/receive/internal)
- Message queue length (for receive events)
- Logical clock value

### Explanations
Actions constrained by clock rate: 
- "PROCESSED" events (processing a message from queue)
- "INTERNAL EVENT" events
- "SENT" events

Actions not constrained by clock rate:
- "RECEIVED" events (these happen whenever other VMs send messages)

## Experiments
Run `run_experiments.py` and specify the arguments accordingly:
```bash
python run_experiments.py --config \[default, modified\] --duration \[seconds\] --trials \[num_trials\]
```

Example:
```bash
python run_experiments.py --config default --duration 60 --trials 5
```

By default, the configuation is `default`, the duration is `60 seconds`, and the number of trials is `5`.

Each experiment creates a new directory with the name of the experiment, trial number, and real life time stamp of when that experiment was ran. Inside the experiment directory are the VM log files, each with three machines. 

### Modified configuations
File `config_modified` contains the configuration for the modified experiment, with a smaller variation in the clock cycles and a smaller probability of the event being internal. More specifically:
1. Clock rates are between 3 and 4 ticks/second (smaller variation)
2. Event probabilities:
   - 40% chance to send to one machine (numbers 1-4)
   - 30% chance to send to all machines (numbers 5-7)
   - 30% chance for internal event (numbers 8-10)

This configuration will result in:
- More consistent timing between machines (only 0.5 tick/second difference)
- More communication between machines (70% of events are sends vs 30% internal)
- More frequent broadcast messages (30% vs the original config's 10%)

## Log Analysis

The `analyze_logs.py` script provides comprehensive analysis of experiment results:

### Features

1. System Characteristics Analysis:
   - Clock rates for each VM
   - Message patterns (internal, point-to-point, broadcast, received)
   - Time-based performance metrics

2. Clock Behavior Analysis:
   - Logical clock jumps (size and frequency)
   - Clock drift between machines
   - Time-based drift rates

3. Queue Analysis:
   - Queue lengths over time
   - Queue growth rates
   - Maximum and average queue sizes

4. Message Pattern Analysis:
   - Message type distribution
   - Communication patterns
   - Message processing rates

### Usage

Run the analysis script:
```bash
python analyze_logs.py --config \[default, modified\] --run \[trial number 1-5\]
```

Example:
```bash
python analyze_logs.py --config default --run 4
```

The script will:
1. Analyze a specific experiment run in the `experiments` directory
2. Generate comprehensive statistics and observations
3. Output results to `observations_{config}_{run number}.md`

### Output

The generated `observations_{config}_{run number}.md` file contains:
- System characteristics for each configuration
- Message pattern analysis
- Logical clock behavior analysis
- Queue behavior analysis
- Comparative analysis between configurations