import unittest

from blocktype import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_heading_1(self):
        text = '###### test'
        output = block_to_block_type(text)
        self.assertEqual(output, BlockType.heading) 

    def test_heading_2(self):
        text = '# test'
        output = block_to_block_type(text)
        self.assertEqual(output, BlockType.heading)

    def test_heading_3(self):
        text = '####### test'
        output = block_to_block_type(text)
        self.assertEqual(output, BlockType.paragraph)

    def test_code(self):
        text = '```\ncode text```'
        output = block_to_block_type(text)
        self.assertEqual(output, BlockType.code) 

    def test_quote(self):
        text = '> quote\n>quote'
        output = block_to_block_type(text)
        self.assertEqual(output, BlockType.quote) 

    def test_unordered_list(self):
        text = '- unordered\n- list'
        output = block_to_block_type(text)
        self.assertEqual(output, BlockType.unordered_list) 
       
    def test_ordered_list(self):
        text = '1. ordered\n22. list'
        output = block_to_block_type(text)
        self.assertEqual(output, BlockType.ordered_list) 

    def test_paragraph(self):
        text = 'Regular Paragraph'
        output = block_to_block_type(text)
        self.assertEqual(output, BlockType.paragraph) 
          
    

if __name__ == "__main__":
    unittest.main()