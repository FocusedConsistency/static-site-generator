import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node2", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false_2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_eq_false_3(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.LINK, "https://wikipedia.org")
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://wikipedia.org")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://wikipedia.org")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://wikipedia.org")
        self.assertEqual(
            "TextNode(This is a text node, text, https://wikipedia.org)", repr(node)
        )

if __name__ == "__main__":
    unittest.main()
