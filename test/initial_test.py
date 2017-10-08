import unittest
from binary_tree import Node, BinaryTree


class TestBinaryTree(unittest.TestCase):

    def setUp(self):
        self.bt = BinaryTree()

    def test_type(self):
        """
        object is of type BinaryTree
        """
        self.assertIsInstance(self.bt, BinaryTree)

    def test_size(self):
        """
        check size of tree object
        """
        self.assertEqual(self.bt.size, 0)

if __name__=="__main__":
    unittest.main()
