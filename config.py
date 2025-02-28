"""Configuration settings for the distributed system simulation."""

# Port range for virtual machines to use
BASE_PORT = 5000

# Probability settings
MIN_RANDOM = 1
MAX_RANDOM = 10
SEND_TO_ONE = [1, 2]  # Values that trigger sending to one machine
SEND_TO_ALL = [3]     # Values that trigger sending to all machines

# Clock settings
MIN_CLOCK_RATE = 1
MAX_CLOCK_RATE = 6

# Log directory
LOG_DIR = "logs"

# Network settings
HOST = "127.0.0.1"
