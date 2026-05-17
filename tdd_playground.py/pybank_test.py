from unittest import TestCase
import pybank


class TestValidateEmail(TestCase):

    def test_that_validate_email_function_exist(self):
        pybank.validate_email("ogor@joel.com")
        
    def test_that_email_has_a_minimium_of_8_characters(self):
        is_valid = pybank.validate_email("ogor@joel.com")
        self.assertTrue(is_valid)
        
    def test_that_invalid_email_less_than_8_characters_return_false(self):
        is_invalid = pybank.validate_email("ogo@")
        self.assertFalse(is_invalid)

    def test_that_invalid_email_raise_value_error(self):
        self.assertRaises(ValueError, pybank.validate_email, "joel@ogr.com")
        
        
    def test_that_email_must_contain_special_character(self):
        is_valid = pybank.validate_email("ogor@joel.com")
        self.assertTrue(is_valid)
        
        
