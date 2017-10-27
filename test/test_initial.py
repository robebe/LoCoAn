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
from dag import DirectedAcyclicGraph, InsertException



class DAGInitial(unittest.TestCase):
    """
    test insertion into graph structure for different scenarios
    and keeping track of size variable and Exceptions.
    """

    def setUp(self):
        self.dag = DirectedAcyclicGraph()


    def test_type(self):
        self.assertIsInstance(self.dag, DirectedAcyclicGraph)

    def test_insertion_and_size(self):
        self.assertEqual(self.dag.size, 1)
        self.dag.add_node(3, 1)
        self.dag.add_node(4, 1)
        self.dag.add_root_node(2, 4)
        self.assertEqual(self.dag.size, 4)
        self.assertEqual(len(self.dag.graph), self.dag.size)
        self.assertEqual(len(self.dag.asList()), self.dag.size)
        self.assertRaises(InsertException, self.dag.add_node(4, 1))
        self.dag.add_node(5, 1)
        self.dag.add_node(7, 5)
        self.dag.add_node(6, 5)
        curr_size = self.dag.size
        self.dag.add_node(6, 3)#adding additional edge btw existing nodes
        self.assertEqual(self.dag.size, curr_size)
        self.dag.add_node(7, 3)
        self.dag.add_node(5, 4)
        self.dag.add_root_node(8, 4)

    def test_more_insertion(self):
        self.assertEqual(self.dag.size, 1)
        self.assertRaises(InsertException, self.dag.add_root_node(2,4))
        self.dag.add_node(3, 1)
        self.dag.add_node(5, 1)
        self.dag.add_node(4, 1)
        self.dag.add_root_node(2, 4)
        curr_size = self.dag.size
        self.dag.add_node(3, 4)#adding additional edge btw existing nodes
        self.assertEqual(self.dag.size, curr_size)
        self.dag.add_node(4, 3)
        self.assertEqual(self.dag.size, curr_size)
        self.dag.add_node(2, 1)
        self.assertEqual(self.dag.size, curr_size)

    def test_datatypes(self):
        self.dag.add_node(57, 1)
        with self.assertRaises(ValueError):
            self.dag.add_node("a", 1)
            self.dag.add_root_node("a", 1)
            self.dag.add_node(1.0, 1)
            self.dag.add_node([], 1)

    def test_listrepr(self):
        pass



if __name__=="__main__":
    unittest.main()
