# Logical Clock System Observations - Default Run 5

## Experiment Directory: default_run_5_20250303_191512

## System Characteristics

VM 0:
- Clock rate: 3 ticks/second

VM 1:
- Clock rate: 2 ticks/second

VM 2:
- Clock rate: 4 ticks/second

## Message Patterns

VM 0:
- point-to-point: 28.8% (55 messages)
- internal: 41.9% (80 messages)
- received: 29.3% (56 messages)

VM 1:
- received: 55.7% (68 messages)
- internal: 28.7% (35 messages)
- point-to-point: 15.6% (19 messages)

VM 2:
- internal: 53.0% (133 messages)
- point-to-point: 33.5% (84 messages)
- received: 13.5% (34 messages)

## Clock Behavior

VM 0:
- Average jump size: 2.69
- Maximum jump size: 6
- Number of jumps: 59
- Final clock value: 236

VM 1:
- Average jump size: 3.67
- Maximum jump size: 10
- Number of jumps: 49
- Final clock value: 235

VM 2:
- Average jump size: 2.31
- Maximum jump size: 4
- Number of jumps: 52
- Final clock value: 235

## Queue Behavior

VM 0:
- Average queue length: 0.07
- Maximum queue length: 1
- Queue length measurements: 55

VM 1:
- Average queue length: 0.31
- Maximum queue length: 3
- Queue length measurements: 68

VM 2:
- Average queue length: 0.00
- Maximum queue length: 0
- Queue length measurements: 34

## Clock Drift

Between VM 0 and VM 1:
- Final drift: 1 ticks

Between VM 0 and VM 2:
- Final drift: 1 ticks

Between VM 1 and VM 2:
- Final drift: 0 ticks