import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode("p", "hello mr fancy pants, look at you!", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "hello mr fancy pants, look at you!")
        self.assertEqual(node.props, {"href": "https://www.google.com", "target": "_blank"})
    
    def test_props_to_html(self):
        node = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")

    def test_repr(self):
        node = HTMLNode("p", "hello mr fancy pants, look at you!", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(repr(node), "\ntag: p\nvalue: hello mr fancy pants, look at you!\nchildren: None\nprops: {'href': 'https://www.google.com', 'target': '_blank'}")

    def test_repr_with_children(self):
        child_node_one = HTMLNode("h1", "Welcome to the jungle", None, {"href": "https://www.google.com", "target": "_blank"})
        child_node_two = HTMLNode("h2", "we have fun and games", None, {"href": "https://www.google.com", "target": "_blank"})
        parent_node = HTMLNode(None, None, [child_node_one, child_node_two], None)
        self.assertEqual(repr(parent_node), "\ntag: None\nvalue: None\nchildren: Welcome to the jungle, we have fun and games\nprops: None")

if __name__ == "__main__":
    unittest.main()