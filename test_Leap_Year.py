import unittest
import Leap_Year
class TestLeap_Year(unittest.TestCase):
    def test_NegativeYear(self):                 ## Checking the year is negative or not 
        stri="Year cannot be negative"
        self.assertEqual(Leap_Year.Leap_year1(-2000),stri) 
    def test_divisble_by_four(self):             ## checking the year is divisible by 4
        self.assertEqual(Leap_Year.Leap_year1(2000),True)
        self.assertEqual(Leap_Year.Leap_year1(2001),False)
    def test_Divisible_by_4_not_by_100(self):    ## checking the year is divisible by 4 but not by 100
        self.assertEqual(Leap_Year.Leap_year1(2016),True)
    def test_Divisible_by_100_but_not_400(self): ## checking the year divisible by 100 but not by 400
         self.assertEqual(Leap_Year.Leap_year1(1900),False)

        
if __name__ == '__main__':
    unittest.main()