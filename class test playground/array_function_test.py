from unittest import TestCase

import array_function

class TestRange(TestCase):
    
    def test_that_list_input_returns_range(self):
        array_function.range_output({2,5,7,9,20})
