from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            split_nodes = []
            split_text = node.text.split(delimiter)
            if len(split_text) % 2 == 0:
                raise ValueError("Invalid markdown, delimeter not closed")
            for i, item in enumerate(split_text):
                if item == "":
                    continue
                if i % 2 == 0:
                    split_nodes.append(TextNode(item, TextType.TEXT))
                else:
                    split_nodes.append(TextNode(item, text_type))
            new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            images = extract_markdown_images(node.text)
            if images == []:
                new_nodes.append(node)
                continue
            original_text = node.text
            for image in images:
                image_alt = image[0]
                image_link = image[1]
                image_markdown = f"![{image_alt}]({image_link})"
                text_split = original_text.split(image_markdown, 1)
                if len(text_split) != 2:
                    raise ValueError("invalid markdown, link section not closed")
                before_image = text_split[0]
                after_image = text_split[1]
                if before_image != "":
                    new_nodes.append(TextNode(before_image, TextType.TEXT))
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
                original_text = after_image
            if original_text != "":
                new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            links = extract_markdown_links(node.text)
            if links == []:
                new_nodes.append(node)
                continue
            original_text = node.text
            for link in links:
                link_alt = link[0]
                link_addr = link[1]
                link_markdown = f"[{link_alt}]({link_addr})"
                text_split = original_text.split(link_markdown, 1)
                if len(text_split) != 2:
                    raise ValueError("invalid markdown, link section not closed")
                before_link = text_split[0]
                after_link = text_split[1]
                if before_link != "":
                    new_nodes.append(TextNode(before_link, TextType.TEXT))
                new_nodes.append(TextNode(link_alt, TextType.LINK, link_addr))
                original_text = after_link
            if original_text != "":
                new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    after_image_split = split_nodes_image(nodes)
    after_link_split = split_nodes_link(after_image_split)
    after_bold_split = split_nodes_delimiter(after_link_split, "**", TextType.BOLD)
    after_italic_split = split_nodes_delimiter(after_bold_split, "_", TextType.ITALIC)
    after_code_split = split_nodes_delimiter(after_italic_split, "`", TextType.CODE)
    return after_code_split
