# Logical Clock System Observations - Modified Run 5

## Experiment Directory: modified_run_5_20250303_193447

## System Characteristics

VM 0:
- Clock rate: 4 ticks/second

VM 1:
- Clock rate: 4 ticks/second

VM 2:
- Clock rate: 3 ticks/second

## Message Patterns

VM 0:
- point-to-point: 57.5% (164 messages)
- received: 42.5% (121 messages)

VM 1:
- point-to-point: 73.2% (229 messages)
- received: 26.8% (84 messages)

VM 2:
- received: 94.8% (199 messages)
- point-to-point: 5.2% (11 messages)

## Clock Behavior

VM 0:
- Average jump size: 2.96
- Maximum jump size: 12
- Number of jumps: 57
- Final clock value: 234

VM 1:
- Average jump size: 3.92
- Maximum jump size: 18
- Number of jumps: 52
- Final clock value: 237

VM 2:
- Average jump size: 2.61
- Maximum jump size: 7
- Number of jumps: 18
- Final clock value: 199

## Queue Behavior

VM 0:
- Average queue length: 0.01
- Maximum queue length: 1
- Queue length measurements: 121

VM 1:
- Average queue length: 0.02
- Maximum queue length: 1
- Queue length measurements: 84

VM 2:
- Average queue length: 14.95
- Maximum queue length: 29
- Queue length measurements: 169

## Clock Drift

Between VM 0 and VM 1:
- Final drift: 3 ticks

Between VM 0 and VM 2:
- Final drift: 35 ticks

Between VM 1 and VM 2:
- Final drift: 38 ticks