"""Test configuration for logical clocks implementation."""

# Network configuration
HOST = 'localhost'
BASE_PORT = 8000

# Clock rates (ticks per second)
MIN_CLOCK_RATE = 1
MAX_CLOCK_RATE = 6

# Random number ranges for events
MIN_RANDOM = 1
MAX_RANDOM = 10
SEND_TO_ONE = [1, 2, 3]  # Numbers that trigger send to one machine
SEND_TO_ALL = [4, 5]     # Numbers that trigger send to all machines

# Logging configuration
LOG_DIR = "test_logs"
