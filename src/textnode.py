from enum import Enum

class TextType(Enum):
    BOLD= "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    TEXT = "text"

class TextNode():
    def __init__(self,text:str,text_type:TextType,url:str| None =None):
        self.text= text
        self.text_type= text_type
        self.url = url

    def __eq__(self, node: "TextNode"):
        if self.text == node.text and self.text_type == node.text_type and self.url == node.url:
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text},{self.text_type.value},{self.url})"