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

from dag import DirectedAcyclicGraph

class DAG_LCA(unittest.TestCase):
    """
    test lowest common ancestor function of directed acyclic graph structure
    """

    def setUp(self):
        self.dag = DirectedAcyclicGraph()
        self.dag.add_node(2,1)
        self.dag.add_node(3,1)
        self.dag.add_node(4,2)
        self.dag.add_node(5,2)
        self.dag.add_node(5,3)
        self.dag.add_node(6,3)
        self.dag.add_node(7,4)
        self.dag.add_node(8,4)
        self.dag.add_node(9,5)
        self.dag.add_node(10,5)
        self.dag.add_node(9,6)
        self.dag.add_node(10,6)
        self.dag.add_node(11,9)
        self.dag.add_node(11,10)
        self.dag.add_root_node(12,4)

    def test_lca(self):
        self.assertEqual(self.dag.getLCA(9,11), [9])
        self.assertEqual(self.dag.getLCA(11,9), [9])
        self.assertEqual(self.dag.getLCA(9,10), [5,6])
        self.assertEqual(self.dag.getLCA(10,3), [3])
        self.assertEqual(self.dag.getLCA(7,10), [2])
        self.assertEqual(self.dag.getLCA(12,10), [])


if __name__=="__main__":
    unittest.main()
