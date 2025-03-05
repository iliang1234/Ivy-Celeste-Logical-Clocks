# Logical Clock System Observations - Default Run 3

## Experiment Directory: default_run_3_20250303_191308

## System Characteristics

VM 0:
- Clock rate: 6 ticks/second

VM 1:
- Clock rate: 4 ticks/second

VM 2:
- Clock rate: 6 ticks/second

## Message Patterns

VM 0:
- internal: 50.3% (186 messages)
- point-to-point: 27.6% (102 messages)
- received: 22.2% (82 messages)

VM 1:
- received: 40.1% (99 messages)
- point-to-point: 22.3% (55 messages)
- internal: 37.7% (93 messages)

VM 2:
- point-to-point: 29.1% (109 messages)
- received: 22.7% (85 messages)
- internal: 48.3% (181 messages)

## Clock Behavior

VM 0:
- Average jump size: 2.37
- Maximum jump size: 6
- Number of jumps: 67
- Final clock value: 360

VM 1:
- Average jump size: 2.95
- Maximum jump size: 10
- Number of jumps: 85
- Final clock value: 359

VM 2:
- Average jump size: 2.46
- Maximum jump size: 7
- Number of jumps: 63
- Final clock value: 360

## Queue Behavior

VM 0:
- Average queue length: 0.00
- Maximum queue length: 0
- Queue length measurements: 82

VM 1:
- Average queue length: 0.13
- Maximum queue length: 1
- Queue length measurements: 99

VM 2:
- Average queue length: 0.07
- Maximum queue length: 1
- Queue length measurements: 85

## Clock Drift

Between VM 0 and VM 1:
- Final drift: 1 ticks

Between VM 0 and VM 2:
- Final drift: 0 ticks

Between VM 1 and VM 2:
- Final drift: 1 ticks