#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import unittest
import random
import os, sys
src_path = os.path.abspath(os.path.join('..','src'))
sys.path.append(src_path)
from binary_tree import Node, BinaryTree



class BinaryTreeInitial(unittest.TestCase):
    """
    This inital test script is supposed to test basic
    insertion for the BinaryTree class.
    """

    def setUp(self):
        self.bt = BinaryTree()
        #self.numbers = [random.randint(0,100) for i in range(10)]
        #self.numbers = [50, 43, 29, 52, 53, 62, 15, 33, 76, 10]

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
        self.bt.insertNode(3)
        self.assertEqual(self.bt.size, 1)
        self.bt.insertNode(2)
        self.bt.insertNode(9)
        self.bt.insertNode(1)
        self.assertEqual(self.bt.size, 4)

    def test_leftist_insertion_order(self):
        numbers = [50, 43, 29, 52, 53, 62, 15, 33, 76, 10,10]
        self.assertEqual(self.bt.size, 0)
        for num in numbers:
            self.bt.insertNode(num)
        self.assertEqual(self.bt.size, len(numbers))
        self.assertTrue(self.bt.root.val==50)
        self.assertTrue(self.bt.root.left.val==43)
        self.assertTrue(self.bt.root.left.left.val==29)
        self.assertTrue(self.bt.root.left.left.left.val==15)
        self.assertTrue(self.bt.root.left.left.right.val==33)
        self.assertTrue(self.bt.root.left.left.left.left.val==10)
        self.assertTrue(self.bt.root.left.left.left.left.left.val==10)
        self.assertTrue(self.bt.root.right.val==52)
        self.assertTrue(self.bt.root.right.right.val==53)
        self.assertTrue(self.bt.root.right.right.right.val==62)
        self.assertTrue(self.bt.root.right.right.right.right.val==76)


if __name__=="__main__":
    unittest.main()
