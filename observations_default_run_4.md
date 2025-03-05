# Logical Clock System Observations - Default Run 4

## Experiment Directory: default_run_4_20250303_191410

## System Characteristics

VM 0:
- Clock rate: 5 ticks/second

VM 1:
- Clock rate: 4 ticks/second

VM 2:
- Clock rate: 6 ticks/second

## Message Patterns

VM 0:
- internal: 50.3% (156 messages)
- received: 25.5% (79 messages)
- point-to-point: 24.2% (75 messages)

VM 1:
- point-to-point: 21.1% (52 messages)
- received: 35.6% (88 messages)
- internal: 43.3% (107 messages)

VM 2:
- internal: 52.6% (200 messages)
- point-to-point: 28.9% (110 messages)
- received: 18.4% (70 messages)

## Clock Behavior

VM 0:
- Average jump size: 2.48
- Maximum jump size: 5
- Number of jumps: 85
- Final clock value: 361

VM 1:
- Average jump size: 2.98
- Maximum jump size: 8
- Number of jumps: 83
- Final clock value: 361

VM 2:
- Average jump size: 2.36
- Maximum jump size: 5
- Number of jumps: 69
- Final clock value: 364

## Queue Behavior

VM 0:
- Average queue length: 0.03
- Maximum queue length: 1
- Queue length measurements: 79

VM 1:
- Average queue length: 0.10
- Maximum queue length: 1
- Queue length measurements: 88

VM 2:
- Average queue length: 0.01
- Maximum queue length: 1
- Queue length measurements: 70

## Clock Drift

Between VM 0 and VM 1:
- Final drift: 0 ticks

Between VM 0 and VM 2:
- Final drift: 3 ticks

Between VM 1 and VM 2:
- Final drift: 3 ticks