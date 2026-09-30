from enum import Enum
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import ParentNode

def markdown_to_blocks(markdown):
    markdown_blocks = markdown.split("\n\n")
    blocks = []
    for block in markdown_blocks:
        if block == "":
            continue
        blocks.append(block.strip())
    return blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block_text):
    if block_text.startswith("#"):
        hashtag_count = len(block_text) - len(block_text.lstrip('#'))
        if (hashtag_count != len(block_text) and
            1 <= hashtag_count <= 6 and 
            block_text[hashtag_count] == " "):
            return BlockType.HEADING

    if block_text.startswith("```\n") and block_text.endswith("```"):
        return BlockType.CODE

    def all_lines_match(lines, prefix):
        for line in lines:
            if not line.startswith(prefix):
                return False
        return True

    lines = block_text.split("\n")
    if all_lines_match(lines, ">"):
        return BlockType.QUOTE

    if all_lines_match(lines, "- "):
        return BlockType.UNORDERED_LIST
    
    olist = True
    for i, line in enumerate(lines, start=1):
        expected = str(i) + ". "
        if not line.startswith(expected):
            olist = False
            break
    if olist:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

    
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        btype = block_to_block_type(block)
        
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []

    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)

    return children

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            cleaned_block = block.replace("\n", " ")
            children = text_to_children(cleaned_block)
            parent = ParentNode("p", children)
            block_nodes.append(parent)
        elif block_type == BlockType.HEADING:
            heading_level = block.find(" ")
            heading_tag = "h" + str(heading_level)
            heading_text = block[heading_level+1:]
            children = text_to_children(heading_text)
            parent = ParentNode(heading_tag, children)
            block_nodes.append(parent)
        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")
            cleaned_lines = []
            for line in lines:
                cleaned = line.lstrip(">").lstrip()
                cleaned_lines.append(cleaned)
            children = text_to_children(' '.join(cleaned_lines))
            parent = ParentNode("blockquote", children)
            block_nodes.append(parent)
        elif block_type == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            item_nodes = []
            for line in lines:
                cleaned = line.lstrip("-").lstrip()
                item_node = ParentNode("li", text_to_children(cleaned))
                item_nodes.append(item_node)
            list_node = ParentNode("ul", item_nodes)
            block_nodes.append(list_node)
        elif block_type == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            item_nodes = []
            for line in lines:
                period_index = line.find(".")
                cleaned = line[period_index + 2:]
                item_node = ParentNode("li", text_to_children(cleaned))
                item_nodes.append(item_node)
            list_node = ParentNode("ol", item_nodes)
            block_nodes.append(list_node)
        elif block_type == BlockType.CODE:
            code_text = block[4:-3]
            code_text_node = TextNode(code_text, TextType.TEXT)
            code_child = text_node_to_html_node(code_text_node)
            code_node = ParentNode("pre", [
                ParentNode("code", [code_child])
            ])
            block_nodes.append(code_node)
    return ParentNode("div", block_nodes)

