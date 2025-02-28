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