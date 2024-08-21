from functools import reduce

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError
        
    def props_to_html(self):
        return "" if self.props == None else reduce(lambda x, key: f"{x} {key}=\"{self.props[key]}\"", self.props, "")
        
    def __repr__(self):
        children_string = "None" if self.children == None else ", ".join([child.value for child in self.children])
        return f"\ntag: {self.tag}\nvalue: {self.value}\nchildren: {children_string}\nprops: {self.props}"