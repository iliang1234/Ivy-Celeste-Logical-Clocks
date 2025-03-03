import os
import shutil
import subprocess
import time
import argparse
from datetime import datetime

def run_experiment(experiment_name, config_file, duration=60):
    """Run a single experiment and organize its logs."""
    # Create experiment directory
    exp_dir = f"experiments/{experiment_name}"
    os.makedirs(exp_dir, exist_ok=True)
    
    # Start the experiment with specified config
    env = os.environ.copy()
    env['CONFIG_PATH'] = os.path.abspath(config_file)
    process = subprocess.Popen(["python", "main.py"], env=env)
    
    # Wait for specified duration
    time.sleep(duration)
    
    # Terminate the experiment
    process.terminate()
    process.wait()
    
    # Move logs to experiment directory
    for i in range(3):
        src = f"logs/machine_{i}.log"
        if os.path.exists(src):
            dst = f"{exp_dir}/machine_{i}.log"
            shutil.move(src, dst)

def main():
    parser = argparse.ArgumentParser(description='Run distributed system experiments')
    parser.add_argument('--config', choices=['default', 'modified'], default='default',
                        help='Configuration to use (default or modified)')
    parser.add_argument('--duration', type=int, default=60,
                        help='Duration of each experiment in seconds')
    parser.add_argument('--trials', type=int, default=5,
                        help='Number of trials to run')
    args = parser.parse_args()

    # Create experiments directory
    os.makedirs("experiments", exist_ok=True)
    
    # Select config file
    config_file = "config.py" if args.config == "default" else "config_modified.py"
    if not os.path.exists(config_file):
        print(f"Error: {config_file} not found!")
        return
    
    print(f"Running {args.trials} experiments with {args.config} configuration...")
    print(f"Each experiment will run for {args.duration} seconds")
    
    for i in range(args.trials):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        exp_name = f"{args.config}_run_{i+1}_{timestamp}"
        print(f"\nStarting experiment {i+1}/{args.trials}: {exp_name}")
        run_experiment(exp_name, config_file, args.duration)
        print(f"Completed experiment {i+1}/{args.trials}")
        time.sleep(2)  # Brief pause between experiments
    
    print("\nAll experiments completed!")

if __name__ == "__main__":
    main()
