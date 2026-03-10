import unittest

from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_good_header(self):
        md = '# header'
        title = extract_title(md)
        self.assertEqual(title, 'header')

    def test_extra_markdown(self):
        md = '# header\n## header 2\nregular text'
        title = extract_title(md)
        self.assertEqual(title, 'header')