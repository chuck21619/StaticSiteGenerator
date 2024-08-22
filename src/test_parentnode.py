import unittest
from parentnode import *
from leafnode import *

class TestParentNode(unittest.TestCase):

    def test_to_html(self):
        node = ParentNode("p",
                          [LeafNode("b", "Bold text"),
                           LeafNode(None, "Normal text"),
                           LeafNode("i", "italic text"),
                           LeafNode(None, "Normal text")])
        print(node.to_html())
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

#   '<b>Bold text</b>Normal text<i>italic text</i>Normal text'
#'<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        
if __name__ == "__main__":
    unittest.main()