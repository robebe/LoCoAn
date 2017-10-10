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
    def setup(self):
        self.bt = BinaryTree()

    def test_lca(self):
        pass

    def test_lca_repr(self):
        pass

if __name__=="__main__":
    unittest.main()
