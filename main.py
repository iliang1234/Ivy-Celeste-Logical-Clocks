"""Main script to run the distributed system simulation."""

import asyncio
import logging
import os
from virtual_machine import VirtualMachine
from config import LOG_DIR

async def main():
    # Create log directory if it doesn't exist
    os.makedirs(LOG_DIR, exist_ok=True)
    
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Number of virtual machines to create
    NUM_MACHINES = 3
    
    # Create virtual machines
    machines = [VirtualMachine(i, NUM_MACHINES) for i in range(NUM_MACHINES)]
    
    # Start servers
    servers = await asyncio.gather(
        *[machine.start_server() for machine in machines]
    )
    
    # Allow time for all servers to start
    await asyncio.sleep(1)
    
    # Connect machines to each other
    await asyncio.gather(
        *[machine.connect_to_others() for machine in machines]
    )
    
    # Run all machines
    try:
        await asyncio.gather(
            *[machine.run() for machine in machines]
        )
    except KeyboardInterrupt:
        # Clean shutdown
        for server in servers:
            server.close()
            await server.wait_closed()
        
        for machine in machines:
            for writer in machine.connections.values():
                writer.close()
                await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
