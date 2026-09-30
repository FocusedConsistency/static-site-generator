import unittest

from block_markdown import (
    markdown_to_blocks,
    BlockType,
    block_to_block_type,
    markdown_to_html_node
)


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type_heading_1(self):
        md = "# This is a level 1 heading"
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.HEADING
        )

    def test_block_to_block_type_heading_2(self):
        md = "###### This is a level 6 heading"
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.HEADING
        )

    def test_block_to_block_type_heading_3(self):
        md = "# "
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.HEADING
        )

    def test_block_to_block_type_paragraph_1(self):
        md = "####### This is a paragraph with seven hashtags"
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.PARAGRAPH
        )

    def test_block_to_block_type_paragraph_2(self):
        md = "#This is a paragraph with a hashtag"
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.PARAGRAPH
        )

    def test_block_to_block_type_paragraph_3(self):
        md = "#"
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.PARAGRAPH
        )
    
    def test_block_to_block_type_paragraph_4(self):
        md = """This is a paragraph"""
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.PARAGRAPH
        )

    def test_block_to_block_type_code_1(self):
        md = """```
def func():
    pass
```"""
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.CODE
        )

    def test_block_to_block_type_code_2(self):
        md = """```

```"""
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.CODE
        )

    def test_block_to_block_type_code_3(self):
        md = """```
```"""
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.CODE
        )

    def test_block_to_block_type_code_4(self):
        md = """```
def func():
    pass
"""
        block_type = block_to_block_type(md)
        self.assertNotEqual(
            block_type,
            BlockType.CODE
        )

    def test_block_to_block_type_code_5(self):
        md = """```"""
        block_type = block_to_block_type(md)
        self.assertNotEqual(
            block_type,
            BlockType.CODE
        )

    def test_block_to_block_type_quote_1(self):
        md = """> one"""
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.QUOTE
        )

    def test_block_to_block_type_quote_2(self):
        md = """> one
> two
> three"""
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.QUOTE
        )

    def test_block_to_block_type_quote_3(self):
        md = """> """
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.QUOTE
        )

    def test_block_to_block_type_quote_4(self):
        md = """>"""
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.QUOTE
        )

    def test_block_to_block_type_quote_5(self):
        md = """> one

> three"""
        block_type = block_to_block_type(md)
        self.assertNotEqual(
            block_type,
            BlockType.QUOTE
        )

    def test_block_to_block_type_ulist_1(self):
        md = """- one"""
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.UNORDERED_LIST
        )

    def test_block_to_block_type_ulist_2(self):
        md = """- one
- two
- three"""
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.UNORDERED_LIST
        )
    
    def test_block_to_block_type_ulist_3(self):
        md = """- one

- three"""
        block_type = block_to_block_type(md)
        self.assertNotEqual(
            block_type,
            BlockType.UNORDERED_LIST
        )

    def test_block_to_block_type_ulist_4(self):
        md = """-one"""
        block_type = block_to_block_type(md)
        self.assertNotEqual(
            block_type,
            BlockType.UNORDERED_LIST
        )

    def test_block_to_block_type_olist_1(self):
        md = """1. one"""
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.ORDERED_LIST
        )

    def test_block_to_block_type_olist_2(self):
        md = """1. one
2. two
3. three"""
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.ORDERED_LIST
        )
    
    def test_block_to_block_type_olist_3(self):
        md = """1. one
2. two
3. three
4. four
5. five
6. six
7. seven
8. eight
9. nine
10. ten"""
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType.ORDERED_LIST
        )

    def test_block_to_block_type_olist_4(self):
        md = """1. one

2. two"""
        block_type = block_to_block_type(md)
        self.assertNotEqual(
            block_type,
            BlockType.ORDERED_LIST
        )

    def test_block_to_block_type_olist_5(self):
        md = """1. one
3. two"""
        block_type = block_to_block_type(md)
        self.assertNotEqual(
            block_type,
            BlockType.ORDERED_LIST
        )

    def test_block_to_block_type_olist_6(self):
        md = """2. one"""
        block_type = block_to_block_type(md)
        self.assertNotEqual(
            block_type,
            BlockType.ORDERED_LIST
        )
    
    def test_block_to_block_type_olist_7(self):
        md = """1 one"""
        block_type = block_to_block_type(md)
        self.assertNotEqual(
            block_type,
            BlockType.ORDERED_LIST
        )

    def test_block_to_block_type_olist_8(self):
        md = """1.one"""
        block_type = block_to_block_type(md)
        self.assertNotEqual(
            block_type,
            BlockType.ORDERED_LIST
        )

    def test_single_paragraph(self):
        md = "A calm forest."
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><p>A calm forest.</p></div>"
        )
    
    def test_heading(self):
        md = "## Forest Guide"
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><h2>Forest Guide</h2></div>"
        )

    def test_quote(self):
        md = """> The forest is green,
> peaceful and calm"""
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><blockquote>The forest is green, peaceful and calm</blockquote></div>"
        )

    def test_unordered_list(self):
        md = """- First tree
- Second tree"""
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><ul><li>First tree</li><li>Second tree</li></ul></div>"
        )

    def test_ordered_list(self):
        md = """1. First forest
2. Second forest"""
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><ol><li>First forest</li><li>Second forest</li></ol></div>"
        )

    def test_code_block(self):
        md = """```
# adds _plus_ **one**
def plus_one(x)
    return x + 1
```"""
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            """<div><pre><code># adds _plus_ **one**
def plus_one(x)
    return x + 1
</code></pre></div>"""
        )
    
if __name__ == "__main__":
    unittest.main()
