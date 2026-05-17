import unittest
import max_numberf.py

class TestMaxNumberFunction(unittest.TestCase):

    def test_that_max_number_function_exists(self):
        functionmax_numberf.largest_number(3,6,7) 
        
    def test_that_max_number_function_return_correct_result(self):
        actual = max_numberf.largest_number(3,6,7)
        expected = 7
        self.assertEqual(actual, expected)  
        actual = max_numberf.largest_number(3,6,2)
        expected = 6
        self.assertEqual(actual, expected)  
        
    def test_that_max_number
        actual = max_numberf.largest_number(3,6,2)
        expected = 'invalid input'
        self.assertEqual(actual, expected)  
        
