import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from validate_skill import parse_frontmatter  # noqa: E402


class ParseFrontmatterTest(unittest.TestCase):
    def test_single_line_description(self):
        fields = parse_frontmatter("---\nname: x\ndescription: one line\n---\n")
        self.assertEqual(fields["description"], "one line")

    def test_folded_block_description(self):
        text = "---\nname: x\ndescription: >-\n  first part\n  second part\n---\n"
        self.assertEqual(parse_frontmatter(text)["description"], "first part second part")

    def test_plain_multiline_description(self):
        text = "---\nname: x\ndescription: first part\n  second part\nversion: 1\n---\n"
        fields = parse_frontmatter(text)
        self.assertEqual(fields["description"], "first part second part")
        self.assertEqual(fields["version"], "1")


if __name__ == "__main__":
    unittest.main()
