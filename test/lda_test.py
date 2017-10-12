#/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import os, sys
src_path = os.path.abspath(os.path.join('..','src'))
sys.path.append(src_path)
from binary_tree import Node, BinaryTree

class BinaryTreeLCA(unittest.TestCase):
    """
    test lowest common ancestor function of BinaryTree class
    """
    def setUp(self):
        self.bt = BinaryTree()
        numbers = [51, 79, 49, 5, 35, 36, 46, 47, 67, 31, 32, 3]
        [self.bt.insertNode(num) for num in numbers]


    def test_lca(self):
        visual_repr = self.bt.visualize()
        for node in visual_repr:
            print(node)
        self.assertEqual(self.bt.getLCA(79,67), 79)
        self.assertEqual(self.bt.getLCA(67,79), 79)
        self.assertEqual(self.bt.getLCA(49,51), 51)
        self.assertEqual(self.bt.getLCA(51,79), 51)
        self.assertEqual(self.bt.getLCA(47,32), 36)
        self.assertEqual(self.bt.getLCA(5,67), 51)

    def test_lca_repr(self):
        pass

if __name__=="__main__":
    unittest.main()
