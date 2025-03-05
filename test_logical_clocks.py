"""Unit tests for the logical clocks implementation."""

import unittest
import asyncio
import json
import os
import sys
from unittest.mock import Mock, patch, AsyncMock
import pytest
import logging

# Set up test config
import test_config
sys.modules['config'] = test_config

from virtual_machine import VirtualMachine

class TestVirtualMachine(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        # Ensure we have a test log directory
        self.test_log_dir = "test_logs"
        os.makedirs(self.test_log_dir, exist_ok=True)
        
        # Create a test VM
        with patch('virtual_machine.LOG_DIR', self.test_log_dir):
            with patch('virtual_machine.random.randint', return_value=4):  # Fix clock rate to 4
                self.vm = VirtualMachine(0, 3)
    
    def tearDown(self):
        """Clean up after each test method."""
        # Clean up log files
        for file in os.listdir(self.test_log_dir):
            os.remove(os.path.join(self.test_log_dir, file))
        os.rmdir(self.test_log_dir)

    def test_init(self):
        """Test virtual machine initialization."""
        self.assertEqual(self.vm.id, 0)
        self.assertEqual(self.vm.total_machines, 3)
        self.assertEqual(self.vm.logical_clock, 0)
        self.assertEqual(self.vm.clock_rate, 4)  # Now fixed to 4
        self.assertEqual(self.vm.port, 8000)  # Assuming default base port
        self.assertEqual(len(self.vm.connections), 0)
        self.assertEqual(len(self.vm.received_messages), 0)

    def test_update_logical_clock(self):
        """Test logical clock updates."""
        # Test internal event
        self.vm.update_logical_clock()
        self.assertEqual(self.vm.logical_clock, 1)

        # Test message receipt with lower timestamp
        self.vm.update_logical_clock(0)
        self.assertEqual(self.vm.logical_clock, 2)

        # Test message receipt with higher timestamp
        self.vm.update_logical_clock(5)
        self.assertEqual(self.vm.logical_clock, 6)

    async def test_send_message(self):
        """Test message sending functionality."""
        mock_writer = AsyncMock()
        mock_writer.write = Mock()  # Make write synchronous since we don't need to test its async behavior
        mock_writer.drain = AsyncMock()
        self.vm.connections[1] = mock_writer

        # Send a message to VM 1
        await self.vm.send_message([1])

        # Verify the message was sent
        self.assertTrue(mock_writer.write.called)
        self.assertTrue(mock_writer.drain.called)

        # Verify message format
        calls = mock_writer.write.call_args_list
        self.assertEqual(len(calls), 2)  # Should be called twice: once for length, once for message

        # Verify message content
        msg_bytes = calls[1][0][0]
        message = json.loads(msg_bytes.decode())
        self.assertEqual(message['sender'], 0)
        self.assertIsInstance(message['clock'], int)

    async def test_handle_connection(self):
        """Test handling incoming connections."""
        # Create mock reader and writer
        reader = AsyncMock()
        writer = AsyncMock()

        # Prepare test message
        test_message = {
            'sender': 1,
            'clock': 5
        }
        msg_bytes = json.dumps(test_message).encode()
        msg_length = len(msg_bytes)
        length_bytes = msg_length.to_bytes(4, 'big')

        # Configure mock reader to return our test message
        reader.read.side_effect = [
            length_bytes,  # First read gets length
            msg_bytes,    # Second read gets message
            b''          # Third read to simulate connection close
        ]

        # Start connection handler
        handler_task = asyncio.create_task(
            self.vm.handle_connection(reader, writer)
        )

        # Wait a bit for message processing
        await asyncio.sleep(0.1)

        # Check if message was queued
        message = await self.vm.message_queue.get()
        self.assertEqual(message['sender'], 1)
        self.assertEqual(message['clock'], 5)

        # Clean up
        handler_task.cancel()
        try:
            await handler_task
        except asyncio.CancelledError:
            pass

    async def test_run_internal_event(self):
        """Test VM's run loop with internal event."""
        # Create a log handler to capture log messages
        log_messages = []
        
        class TestHandler(logging.Handler):
            def emit(self, record):
                log_messages.append(record.getMessage())
        
        handler = TestHandler()
        self.vm.logger.addHandler(handler)

        # Mock random.randint to always return 7 (internal event)
        with patch('virtual_machine.random.randint', return_value=7):
            # Create a task for the run method
            run_task = asyncio.create_task(self.vm.run())

            # Wait until we see the internal event log
            start_time = asyncio.get_event_loop().time()
            while not any("INTERNAL EVENT" in msg for msg in log_messages):
                await asyncio.sleep(0.1)
                if asyncio.get_event_loop().time() - start_time > 1.0:
                    self.fail("Timeout waiting for internal event")

            # Check that logical clock was incremented
            self.assertTrue(self.vm.logical_clock > 0)

            # Clean up
            run_task.cancel()
            try:
                await run_task
            except asyncio.CancelledError:
                pass

class TestMain(unittest.IsolatedAsyncioTestCase):
    async def test_main_setup(self):
        """Test main setup and machine creation."""
        from main import main

        # Create mock VMs
        mock_vms = []
        for i in range(3):
            mock_vm = AsyncMock()
            mock_vm.start_server = AsyncMock(return_value=AsyncMock())
            mock_vm.connect_to_others = AsyncMock()
            mock_vm.run = AsyncMock(side_effect=asyncio.CancelledError)  # Simulate clean exit
            mock_vms.append(mock_vm)
        
        with patch('main.VirtualMachine') as mock_vm_class:
            mock_vm_class.side_effect = mock_vms

            # Run main (it will exit due to CancelledError)
            try:
                await main()
            except asyncio.CancelledError:
                pass

            # Verify VMs were created and methods were called
            self.assertEqual(mock_vm_class.call_count, 3)
            for mock_vm in mock_vms:
                mock_vm.start_server.assert_called_once()
                mock_vm.connect_to_others.assert_called_once()
                mock_vm.run.assert_called_once()

if __name__ == '__main__':
    pytest.main([__file__])
