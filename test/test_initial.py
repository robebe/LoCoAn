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
from dag import DirectedAcyclicGraph



class DAGInitial(unittest.TestCase):
    """
    this inital test script is supposed to test basic
    insertion for the directed acyclic graph structure
    """

    def setUp(self):
        self.dag = DirectedAcyclicGraph()


    def test_type(self):
        """
        object is of type DirectedAcyclicGraph
        """
        self.assertIsInstance(self.dag, DirectedAcyclicGraph)

    def test_insertion_and_size(self):

        self.assertEqual(self.dag.size, 1)
        self.dag.add_node(3, 1)
        self.dag.add_node(4, 1)
        self.dag.add_root_node(2, 4)
        self.assertEqual(self.dag.size, 4)

    def test_datatypes(self):
        pass



if __name__=="__main__":
    unittest.main()
