import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_in(self):
        node = HTMLNode("p", "text", "em")
        self.assertIn("p", repr(node))

    def test_in_2(self):
        node = HTMLNode("p", "text", "em")
        self.assertIn("text", repr(node))

    def test_eq(self):
        node = HTMLNode(props={"href": "https://www.wikipedia.org"})
        self.assertEqual(node.props_to_html(), ' href="https://www.wikipedia.org"')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "A link", {"href": "https://www.wikipedia.org"})
        self.assertEqual(node.to_html(), '<a href="https://www.wikipedia.org">A link</a>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()