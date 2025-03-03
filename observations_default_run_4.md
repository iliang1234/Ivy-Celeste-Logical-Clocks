# Logical Clock System Observations - Default Run 4

## Experiment Directory: default_run_4_20250303_142705

## System Characteristics

VM 0:
- Clock rate: 1 ticks/second

VM 1:
- Clock rate: 6 ticks/second

VM 2:
- Clock rate: 3 ticks/second

## Message Patterns

VM 0:
- received: 100.0% (85 messages)

VM 1:
- point-to-point: 33.3% (127 messages)
- internal: 60.9% (232 messages)
- received: 5.8% (22 messages)

VM 2:
- internal: 41.9% (78 messages)
- received: 34.4% (64 messages)
- point-to-point: 23.7% (44 messages)

## Clock Behavior

VM 0:
- Average jump size: 4.83
- Maximum jump size: 16
- Number of jumps: 41
- Final clock value: 216

VM 1:
- Average jump size: 2.33
- Maximum jump size: 6
- Number of jumps: 70
- Final clock value: 351

VM 2:
- Average jump size: 3.99
- Maximum jump size: 11
- Number of jumps: 69
- Final clock value: 348

## Queue Behavior

VM 0:
- Average queue length: 17.64
- Maximum queue length: 28
- Queue length measurements: 58

VM 1:
- Average queue length: 0.00
- Maximum queue length: 0
- Queue length measurements: 22

VM 2:
- Average queue length: 0.20
- Maximum queue length: 2
- Queue length measurements: 64

## Clock Drift

Between VM 0 and VM 1:
- Final drift: 135 ticks

Between VM 0 and VM 2:
- Final drift: 132 ticks

Between VM 1 and VM 2:
- Final drift: 3 ticks