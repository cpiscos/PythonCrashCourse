import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Middle name work?"""
        formatted_middle_name = get_formatted_name('Wolfgang', 'Mozart', 'amadeus')
        self.assertEqual(formatted_middle_name, 'Wolfgang Amadeus Mozart')
