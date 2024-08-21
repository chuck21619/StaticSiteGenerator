from htmlnode import *

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("missing tag")
        if self.children == None:
            raise ValueError("missing children")
        
        children_string = "".join([child.to_html() for child in self.children])
        return f"<{self.tag}>{children_string}</{self.tag}>"
        