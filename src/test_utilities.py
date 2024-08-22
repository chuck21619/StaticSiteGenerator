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

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        value = extract_markdown_images(text)
        expected_value = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(value, expected_value)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        value = extract_markdown_links(text)
        expected_value = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(value, expected_value)
        
if __name__ == "__main__":
    unittest.main()