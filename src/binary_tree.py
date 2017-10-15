#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

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
        a value of type int, string or float should be inserted
        values will be inserted in ascending order from left to right
        into the tree structure
        """
        if not(type(val) == int or type(val) == str or type(val) == float):
            raise(ValueError('Only values of type int, string or float permitted.'))
        try:
            self.root = self._treeInsert(self.root, val)
            self.size += 1
        except TypeError as e:
            print("Incompatible data type insertion:\n",e)

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


    def asList(self):
        """
        simple list representation of tree
        returns list of tuples, each containing the node value and an integer value indicating the level
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

    def getLCA(self, val1, val2, string_repr=False):
        """
        returns LCA of node1 and node2
        """
        try:
            lca = self._treeLCA(self.root, val1, val2).val
            if string_repr:
                return 'LCA({},{}) = {}'.format(val1, val2, lca)
            return lca
        except AttributeError as e:
            print('The numbers specified ({},{}) do not occur in the tree:\n'.format(val1, val2), e)

    def _treeLCA(self, top, val1, val2):
        if not top:
            return None
        if top.val == val1 or top.val == val2:
            return top
        left_lca = self._treeLCA(top.left, val1, val2)
        right_lca = self._treeLCA(top.right, val1, val2)
        if left_lca and right_lca:
            return top
        return left_lca or right_lca

    def visualize(self):
        """
        tree-like representation of the tree structure
        """
        return self._treeVisualize(self.root)

    def _treeVisualize(self, node, ret=[], space=0):
        if node:
            self._treeVisualize(node.left, ret, space=space+4)
            ret.append('{}{}{}'.format(" "*space, "-->", node.val))
            self._treeVisualize(node.right, ret, space=space+4)
        return ret
