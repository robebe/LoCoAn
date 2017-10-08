#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Node:
    def __init__(self,val):
        """
        Minimalistic defintion of a Node object.
        Each node of the tree is defined by a value (either a number or a string).
        Navigation through the tree structure is done by accessing the left or right
        child of the node.
        """
        self.val = val
        self.left = self.right = None
