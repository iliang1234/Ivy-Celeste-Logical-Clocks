"""Virtual Machine implementation with Lamport's Logical Clock."""

import asyncio
import json
import logging
import os
import random
import time
from datetime import datetime
from typing import List, Dict, Optional

from config import *

class VirtualMachine:
    def __init__(self, machine_id: int, total_machines: int):
        """Initialize a virtual machine with given ID and total number of machines in the system."""
        self.id = machine_id
        self.total_machines = total_machines
        self.logical_clock = 0
        self.clock_rate = random.randint(MIN_CLOCK_RATE, MAX_CLOCK_RATE)
        self.message_queue = asyncio.Queue()
        self.connections: Dict[int, asyncio.StreamWriter] = {}
        self.port = BASE_PORT + machine_id
        self.received_messages = set()  # Track unique messages
        self.queue_lock = asyncio.Lock()  # Lock for queue operations
        
        # Setup logging
        os.makedirs(LOG_DIR, exist_ok=True)
        self.logger = logging.getLogger(f"VM_{machine_id}")
        self.logger.setLevel(logging.INFO)
        fh = logging.FileHandler(os.path.join(LOG_DIR, f"machine_{machine_id}.log"))
        fh.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
        self.logger.addHandler(fh)
        
        self.logger.info(f"Initialized VM {machine_id} with clock rate {self.clock_rate} ticks/second")

    async def start_server(self):
        """Start the server to listen for incoming connections."""
        server = await asyncio.start_server(
            self.handle_connection, HOST, self.port
        )
        self.logger.info(f"Server started on {HOST}:{self.port}")
        return server

    async def connect_to_others(self):
        """Connect to other virtual machines."""
        for i in range(self.total_machines):
            if i != self.id:
                try:
                    reader, writer = await asyncio.open_connection(
                        HOST, BASE_PORT + i
                    )
                    self.connections[i] = writer
                    self.logger.info(f"Connected to VM {i}")
                except Exception as e:
                    self.logger.error(f"Failed to connect to VM {i}: {e}")

    async def handle_connection(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        """Handle incoming connections and messages."""
        while True:
            try:
                # Read message length first (4 bytes)
                length_data = await reader.read(4)
                if not length_data:
                    break
                    
                msg_length = int.from_bytes(length_data, 'big')
                data = await reader.read(msg_length)
                if not data:
                    break
                
                message = json.loads(data.decode())
                message_id = f"{message['sender']}_{message['clock']}"  # Create unique message ID
                
                # Only process message if we haven't seen it before
                if message_id not in self.received_messages:
                    self.received_messages.add(message_id)
                    async with self.queue_lock:
                        await self.message_queue.put(message)
                        queue_size = self.message_queue.qsize()
                        self.logger.info(
                            f"RECEIVED: Message from VM {message['sender']} "
                            f"with logical time {message['clock']} | "
                            f"Added to queue (now size: {queue_size})"
                        )
                
            except Exception as e:
                self.logger.error(f"Error handling connection: {e}")
                continue  # Don't break on parse errors, try next message

    def update_logical_clock(self, received_time: Optional[int] = None):
        """Update the logical clock based on Lamport's rules."""
        if received_time is not None:
            self.logical_clock = max(self.logical_clock, received_time) + 1
        else:
            self.logical_clock += 1

    async def send_message(self, target_ids: List[int]):
        """Send message to specified target machines."""
        message = {
            'sender': self.id,
            'clock': self.logical_clock
        }
        
        # Encode message
        msg_bytes = json.dumps(message).encode()
        msg_length = len(msg_bytes)
        length_bytes = msg_length.to_bytes(4, 'big')
        
        sent_count = 0
        for target_id in target_ids:
            if target_id in self.connections:
                writer = self.connections[target_id]
                try:
                    # Send length followed by message
                    writer.write(length_bytes)
                    writer.write(msg_bytes)
                    await writer.drain()
                    sent_count += 1
                    self.logger.info(
                        f"SENT: Message to VM {target_id} at logical time {self.logical_clock}"
                    )
                except Exception as e:
                    self.logger.error(f"Failed to send message to VM {target_id}: {e}")
        
        if sent_count > 0:
            self.logger.debug(f"Successfully sent message to {sent_count} machines")

    async def run(self):
        """Main run loop of the virtual machine."""
        while True:
            try:
                # Wait for one clock cycle
                await asyncio.sleep(1 / self.clock_rate)
                
                # Check for messages
                async with self.queue_lock:
                    if not self.message_queue.empty():
                        message = await self.message_queue.get()
                        received_clock = message['clock']
                        queue_size = self.message_queue.qsize()  # Get size while holding lock
                        
                        self.update_logical_clock(received_clock)
                        self.logger.info(
                            f"PROCESSED: Message from VM {message['sender']} | "
                            f"Remaining queue size: {queue_size} | "
                            f"Updated logical clock: {self.logical_clock}"
                        )
                
                    else:
                        # Generate random event
                        event = random.randint(MIN_RANDOM, MAX_RANDOM)
                        
                        if event in SEND_TO_ONE:
                            # Send to one random machine
                            target = random.choice([i for i in range(self.total_machines) if i != self.id])
                            self.update_logical_clock()
                            await self.send_message([target])
                            
                        elif event in SEND_TO_ALL:
                            # Send to all machines
                            self.update_logical_clock()
                            targets = [i for i in range(self.total_machines) if i != self.id]
                            await self.send_message(targets)
                            
                        else:
                            # Internal event
                            self.update_logical_clock()
                            self.logger.info(f"INTERNAL EVENT: Logical clock: {self.logical_clock}")
                        
            except Exception as e:
                self.logger.error(f"Error in run loop: {e}")
                await asyncio.sleep(1)  # Prevent tight error loop
