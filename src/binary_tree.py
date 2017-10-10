#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import random
from node import Node

class BinaryTree:
    def __init__(self):
        """
        The purpose of this program is to implement a leftist binary tree structur
        with all necessary requirements for computation of Lowest Common Ancestor (LCA).
        """
        self.root = None
        self.size = 0

    def insertNode(self, val):
        """
        A value of type number or string should be inserted.
        Once a value type is chosen, all consecutive insertions should be of the same type,
        thereby making it possible to sort the types in descending order from left to right
        into the tree structure.
        """
        self.root = self._treeInsert(self.root, val)
        self.size += 1

    def _treeInsert(self, node, val):
        if node is None:
            return Node(val)
        if (val <= node.val):
            if (node.left is not None):
                self._treeInsert(node.left, val)
            else:
                node.left = Node(val)
        else:
            if (node.right is not None):
                self._treeInsert(node.right, val)
            else:
                node.right = Node(val)
        return self.root

    def visualize(self):
        """
        tree-like representation of the tree structure
        """
        pass

    def asList(self):
        """
        simple list representation of tree.
        returns list of tuples, each containing the node value and an integer value indicating the level
        (eg. if self.root is set to 3 the first item of the list should be (3,0)).
        """
        tree_list = self._treeList(self.root)
        return tree_list

    def _treeList(self, node, ret=[], indx=0):
        if node is None:
            return ret
        else:
            ret.insert(indx, (node.val, indx))
            if node.left or node.right:
                indx +=1
                self._treeList(node.left, ret, indx)
                self._treeList(node.right, ret, indx)
        return ret

    def getLCA(self, node1, node2):
        """
        returns LCA of node1 and node2 (main purpose of this project)
        """
        pass



"""
if __name__=="__main__":
    n1 = Node(3)
    bt = BinaryTree()
    bt.insertNode(n1)
"""
