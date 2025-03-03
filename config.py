"""Configuration settings for the distributed system simulation."""

# Port numbers for each virtual machine
BASE_PORT = 5000

# Clock rate range (ticks per second)
MIN_CLOCK_RATE = 1
MAX_CLOCK_RATE = 6

# Probability settings
MIN_RANDOM = 1
MAX_RANDOM = 10
SEND_TO_ONE = [1, 2]  # 20% chance to send to one
SEND_TO_ALL = [3]     # 10% chance to send to all
# all remaining 4-10 are internal events; 70% chance to internal event

# Clock settings
MIN_CLOCK_RATE = 1
MAX_CLOCK_RATE = 6

# Log directory
LOG_DIR = "logs"

# Network settings
HOST = "127.0.0.1"
