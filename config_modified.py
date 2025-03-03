"""Configuration settings for the distributed system simulation."""

# Port range for virtual machines to use
BASE_PORT = 5000

# Probability settings
MIN_RANDOM = 1
MAX_RANDOM = 10
# Increased external events (send) to reduce internal event probability to 0.3
SEND_TO_ONE = [1, 2, 3, 4]  # 40% chance to send to one
SEND_TO_ALL = [5, 6, 7]     # 30% chance to send to all
# Remaining 30% (8,9,10) are internal events

# Clock settings - smaller variation
MIN_CLOCK_RATE = 3
MAX_CLOCK_RATE = 4

# Log directory
LOG_DIR = "logs"

# Network settings
HOST = "127.0.0.1"
