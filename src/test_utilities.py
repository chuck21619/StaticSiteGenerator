import unittest
from utilities import *
from textnode import *

class TestUtilities(unittest.TestCase):

    def test_split_delimeter(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        expected_nodes = [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word", text_type_text)
        ]
        
        self.assertEqual(new_nodes[0], expected_nodes[0])
        self.assertEqual(new_nodes[1], expected_nodes[1])
        self.assertEqual(new_nodes[2], expected_nodes[2])

        
if __name__ == "__main__":
    unittest.main()