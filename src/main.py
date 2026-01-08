from textnode import TextNode,TextType
from leafnode import LeafNode
import re
#./main.sh

def main():
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None,text_node.text)
        case TextType.BOLD:
            return LeafNode("b",text_node.text)   
        case TextType.ITALIC:
            return LeafNode("i",text_node.text)
        case TextType.CODE:
            return LeafNode("code",text_node.text)
        case TextType.LINK:
            return LeafNode("a",text_node.text,{"href":text_node.url})
        case TextType.IMAGE:
            return LeafNode("img","",{"src":text_node.url,"alt":text_node.text})
        case _:
            raise Exception("Invalid Text type")
def split_nodes_delimiter(old_nodes, delimiter, text_type):
        output = []
        for node in old_nodes:
            if  node.text_type != TextType.TEXT:
                output.append(node)
                continue
            
            partitions= node.text.split(delimiter)
            if len(partitions) % 2 == 0:
                raise ValueError(f"Invalid markdown: missing closing '{delimiter}'")
            
            for i ,partition in enumerate(partitions):
                if partition =="":
                    continue
                if i % 2 == 0:
                    output.append(TextNode(partition, TextType.TEXT))
                else:
                    output.append(TextNode(partition,text_type))

        return output        

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)

    #return tuples list
def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
def split_nodes_image(old_nodes):
    output= []
    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            output.append(node)
            continue
        text = node.text
        images = extract_markdown_images(text)

        for alt,url in images:
            image_markdown = f"![{alt}]({url})"
            before, text = text.split(image_markdown, 1)

            if before:
                output.append(TextNode(before, TextType.TEXT))

            output.append(TextNode(alt, TextType.IMAGE, url))

        if text:
            output.append(TextNode(text, TextType.TEXT))

    return output
def split_nodes_link(old_nodes):
    output= []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            output.append(node)
            continue
        text = node.text
        links = extract_markdown_links(text)

        for alt,url in links:
            link_markdown = f"[{alt}]({url})"
            before, text = text.split(link_markdown, 1)

            if before:
                output.append(TextNode(before, TextType.TEXT))

            output.append(TextNode(alt, TextType.LINK, url))

        if text:
            output.append(TextNode(text, TextType.TEXT))

    return output

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes

main()
