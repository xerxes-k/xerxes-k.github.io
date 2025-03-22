import unittest
from prime import is_prime

class Tests(unittest.TestCase):
    def test_1(self):
        """check that 1 is not prime"""
        self.assertFalse(is_prime(1))    
    
    def test_2(self):
        """check that 2 is prime
        """
        self.assertTrue(is_prime(2))
    
    def test_28(self):
        """check that 28 is not prime
        """
        self.assertFalse(is_prime(28))
        
if __name__ == "__main__":
    unittest.main()
