# Logical Clock System Observations - Modified Run 2

## Experiment Directory: modified_run_2_20250303_193141

## System Characteristics

VM 0:
- Clock rate: 4 ticks/second

VM 1:
- Clock rate: 3 ticks/second

VM 2:
- Clock rate: 4 ticks/second

## Message Patterns

VM 0:
- point-to-point: 64.2% (188 messages)
- received: 35.8% (105 messages)

VM 1:
- received: 100.0% (207 messages)

VM 2:
- point-to-point: 70.4% (214 messages)
- received: 29.6% (90 messages)

## Clock Behavior

VM 0:
- Average jump size: 3.18
- Maximum jump size: 17
- Number of jumps: 60
- Final clock value: 237

VM 1:
- Average jump size: 2.16
- Maximum jump size: 4
- Number of jumps: 19
- Final clock value: 198

VM 2:
- Average jump size: 3.40
- Maximum jump size: 19
- Number of jumps: 58
- Final clock value: 237

## Queue Behavior

VM 0:
- Average queue length: 0.00
- Maximum queue length: 0
- Queue length measurements: 105

VM 1:
- Average queue length: 18.41
- Maximum queue length: 32
- Queue length measurements: 175

VM 2:
- Average queue length: 0.01
- Maximum queue length: 1
- Queue length measurements: 90

## Clock Drift

Between VM 0 and VM 1:
- Final drift: 39 ticks

Between VM 0 and VM 2:
- Final drift: 0 ticks

Between VM 1 and VM 2:
- Final drift: 39 ticks