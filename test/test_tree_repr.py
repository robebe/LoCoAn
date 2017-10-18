#!/usr/bin/env python3
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

class BinaryTreeRepr(unittest.TestCase):
    """
    test representation of BinaryTree class
    """

    def setUp(self):
        self.bt = BinaryTree()
        numbers = [49, 42, 4, 32, 57, 100, 99, 20, 89, 24, 79, 83]
        [self.bt.insertNode(num) for num in numbers]


    def test_listrepr(self):
        list_repr = '[(49, 0), (57, 1), (100, 2), (99, 3), (89, 4), (79, 5), (83, 6), (42, 1), (4, 2), (32, 3), (20, 4), (24, 5)]'
        self.assertEqual(list_repr, str(self.bt.asList()))

    def test_visualization(self):
        visual_repr = self.bt.visualize()
        self.assertTrue(type(visual_repr) is list)
        self.assertEqual(len(visual_repr), self.bt.size)


if __name__=="__main__":
    unittest.main()
