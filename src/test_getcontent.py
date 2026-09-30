import unittest
from gencontent import extract_title
from block_markdown import (
    markdown_to_blocks,
    BlockType,
    block_to_block_type,
    markdown_to_html_node
)



class TestGenContent(unittest.TestCase):
    def test_extract_h1_title(self):
        md = "# This is a level 1 heading"
        title = extract_title(md)
        self.assertEqual(
            title,
            "This is a level 1 heading"
        )

    def test_h1_title_on_second_line(self):
        md = """First Line
# Second Line"""
        title = extract_title(md)
        self.assertEqual(
            title,
            "Second Line"
        )

    def test_padded_title(self):
        md = "#  This is a level 1 heading "
        title = extract_title(md)
        self.assertEqual(
            title,
            "This is a level 1 heading"
        )

    def test_no_h1_title(self):
        md = "## This is a level 2 heading"
        with self.assertRaises(Exception):
            extract_title(md)

if __name__ == "__main__":
    unittest.main()