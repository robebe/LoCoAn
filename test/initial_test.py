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
    this inital test script is supposed to test basic
    insertion for the BinaryTree class
    """

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
        self.bt.insertNode(3)
        self.assertEqual(self.bt.size, 1)
        self.bt.insertNode(2)
        self.bt.insertNode(9)
        self.bt.insertNode(1)
        self.assertEqual(self.bt.size, 4)

    def test_leftist_insertion_order(self):
        """
        test and demonstrate node access via .left/ .right
        """
        numbers = [50, 43, 29, 52, 53, 62, 15, 33, 76, 10, 10]
        self.assertEqual(self.bt.size, 0)
        [self.bt.insertNode(num) for num in numbers]
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

    def test_datatypes(self):
        """
        test insertion for different data types
        """
        with self.assertRaises(ValueError) as warning:
            self.bt.insertNode([1,2,3])
        chars = ['m', 'b', 'a', 'A', 'x', 'f', 'l', 'k', 't', 'T', 'W', 'w']
        [self.bt.insertNode(ch) for ch in chars]
        self.assertEqual(self.bt.root.val, 'm')
        self.assertEqual(self.bt.root.left.val, 'b')
        self.assertEqual(self.bt.root.right.val, 'x')
        self.assertEqual(self.bt.root.left.left.left.val, 'A')
        self.assertEqual(self.bt.root.left.left.left.right.val, 'T')
        #redirect output-stream to skip TypeError message
        _stdout = sys.stdout
        null = open(os.devnull, 'w')
        sys.stdout = null
        self.assertRaises(TypeError, self.bt.insertNode(1))
        null.close()
        sys.stdout = _stdout



if __name__=="__main__":
    unittest.main()
