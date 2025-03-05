# Logical Clock System Observations - Default Run 1

## Experiment Directory: default_run_1_20250303_191104

## System Characteristics

VM 0:
- Clock rate: 4 ticks/second

VM 1:
- Clock rate: 4 ticks/second

VM 2:
- Clock rate: 1 ticks/second

## Message Patterns

VM 0:
- point-to-point: 27.9% (70 messages)
- received: 17.1% (43 messages)
- internal: 55.0% (138 messages)

VM 1:
- point-to-point: 31.2% (79 messages)
- received: 11.9% (30 messages)
- internal: 56.9% (144 messages)

VM 2:
- received: 100.0% (76 messages)

## Clock Behavior

VM 0:
- Average jump size: 2.16
- Maximum jump size: 3
- Number of jumps: 44
- Final clock value: 233

VM 1:
- Average jump size: 2.40
- Maximum jump size: 4
- Number of jumps: 42
- Final clock value: 234

VM 2:
- Average jump size: 4.28
- Maximum jump size: 9
- Number of jumps: 39
- Final clock value: 187

## Queue Behavior

VM 0:
- Average queue length: 0.00
- Maximum queue length: 0
- Queue length measurements: 43

VM 1:
- Average queue length: 0.00
- Maximum queue length: 0
- Queue length measurements: 30

VM 2:
- Average queue length: 8.53
- Maximum queue length: 17
- Queue length measurements: 58

## Clock Drift

Between VM 0 and VM 1:
- Final drift: 1 ticks

Between VM 0 and VM 2:
- Final drift: 46 ticks

Between VM 1 and VM 2:
- Final drift: 47 ticks