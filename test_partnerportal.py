# test_partnerportal.py
"""
Tests for PartnerPortal module.
"""

import unittest
from partnerportal import PartnerPortal

class TestPartnerPortal(unittest.TestCase):
    """Test cases for PartnerPortal class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PartnerPortal()
        self.assertIsInstance(instance, PartnerPortal)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PartnerPortal()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
