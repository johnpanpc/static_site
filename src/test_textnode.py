import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        node3 = TextNode("Something", TextType.LINK, "https://www.boot.dev")
        node4 = TextNode("Something", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(node3, node4)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

        node3 = TextNode("Something", TextType.LINK, "https://www.boot.dev")
        node4 = TextNode("Something", TextType.LINK)
        self.assertNotEqual(node3, node4)


if __name__ == "__main__":
    unittest.main()