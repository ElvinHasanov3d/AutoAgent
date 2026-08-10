# test_autoagent.py
"""
Tests for AutoAgent module.
"""

import unittest
from autoagent import AutoAgent

class TestAutoAgent(unittest.TestCase):
    """Test cases for AutoAgent class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AutoAgent()
        self.assertIsInstance(instance, AutoAgent)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AutoAgent()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
