# test_noncetracker.py
"""
Tests for NonceTracker module.
"""

import unittest
from noncetracker import NonceTracker

class TestNonceTracker(unittest.TestCase):
    """Test cases for NonceTracker class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NonceTracker()
        self.assertIsInstance(instance, NonceTracker)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NonceTracker()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
