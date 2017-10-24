#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import unittest
import os, sys

src_path = os.path.abspath(os.path.join('..','src'))
sys.path.append(src_path)
"""
src_path = os.path.abspath('src')
sys.path.append(src_path)
"""
from binary_tree import Node, BinaryTree



class DAGInitial(unittest.TestCase):
    """
    this inital test script is supposed to test basic
    insertion for the directed acyclic graph structure
    """

    def setUp(self):
        self.dag = DirectedAcyclicGraph(root_val=1)


    def test_type(self):
        """
        object is of type DirectedAcyclicGraph
        """
        self.assertIsInstance(self.dag, DirectedAcyclicGraph)

    def test_insertion_and_size(self):
        """
        node insertion via .left/ .right and size variable
        """
        self.assertEqual(self.dag.size, 1)
        self.dag.insertRight(root, 2)
        self.assertEqual(self.dag.size, 2)
        self.dag.insertLeft(root.right, 5)
        self.dag.insertRight(root.right, 3)
        self.dag.insertRight(root.right.right, 4)
        self.dag.insertLeft(root.right.right, 6)
        self.dag.insertRight(root.right,left, 6)
        self.dag.assertEqual(self.dag.size, 6)
        self.dag.insertRight(root.right.right.right, 7)
        self.dag.insertLeft(root.right.right.right, 8)
        self.dag.insertRight(root.right.left.right, 9)
        self.assertEqual(self.dag.root.right.right.right.left, 9)

    def test_datatypes(self):
        """
        test insertion for different data types
        """
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
        #redirect output-stream to dev/null-device to skip TypeError message
        _stdout = sys.stdout
        null = open(os.devnull, 'w')
        sys.stdout = null
        self.assertRaises(TypeError, self.bt.insertNode(1))
        null.close()
        sys.stdout = _stdout
        """
        pass



if __name__=="__main__":
    unittest.main()
