import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_init(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(node.url, None)
        self.assertEqual(node.text, "This is a text node")
        self.assertEqual(node.text_type, "bold")
    
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_eq2(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", "bold", "www.google.com")
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, www.google.com)")

if __name__ == "__main__":
    unittest.main()