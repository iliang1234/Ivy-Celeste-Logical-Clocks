# Logical Clock System Observations - Default Run 2

## Experiment Directory: default_run_2_20250303_191206

## System Characteristics

VM 0:
- Clock rate: 1 ticks/second

VM 1:
- Clock rate: 4 ticks/second

VM 2:
- Clock rate: 3 ticks/second

## Message Patterns

VM 0:
- received: 97.4% (76 messages)
- internal: 2.6% (2 messages)

VM 1:
- internal: 57.9% (147 messages)
- received: 11.8% (30 messages)
- point-to-point: 30.3% (77 messages)

VM 2:
- point-to-point: 34.5% (67 messages)
- internal: 45.9% (89 messages)
- received: 19.6% (38 messages)

## Clock Behavior

VM 0:
- Average jump size: 4.26
- Maximum jump size: 11
- Number of jumps: 38
- Final clock value: 183

VM 1:
- Average jump size: 2.22
- Maximum jump size: 4
- Number of jumps: 49
- Final clock value: 237

VM 2:
- Average jump size: 3.00
- Maximum jump size: 6
- Number of jumps: 54
- Final clock value: 236

## Queue Behavior

VM 0:
- Average queue length: 6.89
- Maximum queue length: 18
- Queue length measurements: 56

VM 1:
- Average queue length: 0.00
- Maximum queue length: 0
- Queue length measurements: 30

VM 2:
- Average queue length: 0.05
- Maximum queue length: 1
- Queue length measurements: 38

## Clock Drift

Between VM 0 and VM 1:
- Final drift: 54 ticks

Between VM 0 and VM 2:
- Final drift: 53 ticks

Between VM 1 and VM 2:
- Final drift: 1 ticks