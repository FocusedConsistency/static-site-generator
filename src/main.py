from textnode import TextType, TextNode

def main() -> None:
    new_node = TextNode("This is some anchor text", TextType.LINK, "https://wikipedia.org")
    print(new_node)

if __name__ == "__main__":
    main()
