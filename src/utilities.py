from textnode import *
import re

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.extend(old_node)
            continue

        split_strings = old_node.text.split(delimiter)
        if len(split_strings) != 3:
            raise Exception("that's invalid Markdown syntax")
        temp_text_nodes = [
            TextNode(split_strings[0], old_node.text_type, old_node.url),
            TextNode(split_strings[1], text_type, old_node.url),
            TextNode(split_strings[2], old_node.text_type, old_node.url)
        ]
        new_nodes.extend(temp_text_nodes)
    return new_nodes
