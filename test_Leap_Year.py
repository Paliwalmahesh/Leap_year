import unittest
import Leap_Year
class TestLeap_Year(unittest.TestCase):
    def test_NegativeYear(self):                 ## Checking the year is negative or not 
        stri="Year cannot be negative"
        self.assertEqual(Leap_Year.Leap_year1(-2000),stri) 

        
        
if __name__ == '__main__':
    unittest.main()