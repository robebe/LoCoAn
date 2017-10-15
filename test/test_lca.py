#/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import os, sys
"""
src_path = os.path.abspath(os.path.join('..','src'))
sys.path.append(src_path)
"""
src_path = os.path.abspath('src')
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
        self.assertEqual(self.bt.getLCA(79,67), 79)
        self.assertEqual(self.bt.getLCA(67,79), 79)
        self.assertEqual(self.bt.getLCA(49,51), 51)
        self.assertEqual(self.bt.getLCA(51,79), 51)
        self.assertEqual(self.bt.getLCA(47,32), 35)
        self.assertEqual(self.bt.getLCA(5,67), 51)
        #redirect output-stream to dev/null-device to skip TypeError message
        _stdout = sys.stdout
        null = open(os.devnull, 'w')
        sys.stdout = null
        self.assertRaises(AttributeError, self.bt.getLCA(157, 1))
        null.close()
        sys.stdout = _stdout

    def test_lca_repr(self):
        self.assertEqual(self.bt.getLCA(79,67, visualize=True), 'LCA(79,67) = 79')

if __name__=="__main__":
    unittest.main()
