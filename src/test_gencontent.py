import unittest
from gencontent import extract_title

class TestGenContent(unittest.TestCase):
    def test_header(self):
        self.assertEqual(extract_title("# Hello"),"Hello")

    def test_header_striped_whitespace(self):
        self.assertEqual(extract_title("#       Hello"),"Hello")
    
    def test_no_header(self):
        with self.assertRaises(Exception):
            extract_title("No header here")

    def test_wrong_header(self):
        with self.assertRaises(Exception):
            extract_title("## header2 \n\n ### header3 \n\n Just some text")
    
    def test_multiple_blocks_before_header(self):
        self.assertEqual(extract_title("Hi\n\n This \n\n is \n\n # The Title"),"The Title")

    def test_miltiple_header(self):
        self.assertEqual(extract_title("# Title\n\n# Also Title"),"Title")

    def test_none_input(self):
        with self.assertRaises(Exception):
            extract_title(None)


