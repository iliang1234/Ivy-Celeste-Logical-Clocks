# Logical Clock System Observations - Modified Run 1

## Experiment Directory: modified_run_1_20250303_193039

## System Characteristics

VM 0:
- Clock rate: 4 ticks/second

VM 1:
- Clock rate: 4 ticks/second

VM 2:
- Clock rate: 3 ticks/second

## Message Patterns

VM 0:
- point-to-point: 52.4% (150 messages)
- received: 47.6% (136 messages)

VM 1:
- point-to-point: 77.1% (253 messages)
- received: 22.9% (75 messages)

VM 2:
- received: 96.6% (199 messages)
- point-to-point: 3.4% (7 messages)

## Clock Behavior

VM 0:
- Average jump size: 2.65
- Maximum jump size: 13
- Number of jumps: 63
- Final clock value: 240

VM 1:
- Average jump size: 3.53
- Maximum jump size: 26
- Number of jumps: 58
- Final clock value: 233

VM 2:
- Average jump size: 2.37
- Maximum jump size: 5
- Number of jumps: 19
- Final clock value: 198

## Queue Behavior

VM 0:
- Average queue length: 0.00
- Maximum queue length: 0
- Queue length measurements: 135

VM 1:
- Average queue length: 0.04
- Maximum queue length: 1
- Queue length measurements: 75

VM 2:
- Average queue length: 16.44
- Maximum queue length: 33
- Queue length measurements: 171

## Clock Drift

Between VM 0 and VM 1:
- Final drift: 7 ticks

Between VM 0 and VM 2:
- Final drift: 42 ticks

Between VM 1 and VM 2:
- Final drift: 35 ticks