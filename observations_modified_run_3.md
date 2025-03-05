# Logical Clock System Observations - Modified Run 3

## Experiment Directory: modified_run_3_20250303_193243

## System Characteristics

VM 0:
- Clock rate: 4 ticks/second

VM 1:
- Clock rate: 4 ticks/second

VM 2:
- Clock rate: 4 ticks/second

## Message Patterns

VM 0:
- point-to-point: 45.7% (126 messages)
- received: 54.3% (150 messages)

VM 1:
- point-to-point: 48.2% (133 messages)
- received: 51.8% (143 messages)

VM 2:
- point-to-point: 55.8% (163 messages)
- received: 44.2% (129 messages)

## Clock Behavior

VM 0:
- Average jump size: 2.81
- Maximum jump size: 12
- Number of jumps: 48
- Final clock value: 238

VM 1:
- Average jump size: 3.09
- Maximum jump size: 12
- Number of jumps: 46
- Final clock value: 240

VM 2:
- Average jump size: 3.67
- Maximum jump size: 20
- Number of jumps: 42
- Final clock value: 240

## Queue Behavior

VM 0:
- Average queue length: 0.35
- Maximum queue length: 2
- Queue length measurements: 150

VM 1:
- Average queue length: 0.36
- Maximum queue length: 2
- Queue length measurements: 143

VM 2:
- Average queue length: 0.64
- Maximum queue length: 3
- Queue length measurements: 127

## Clock Drift

Between VM 0 and VM 1:
- Final drift: 2 ticks

Between VM 0 and VM 2:
- Final drift: 2 ticks

Between VM 1 and VM 2:
- Final drift: 0 ticks