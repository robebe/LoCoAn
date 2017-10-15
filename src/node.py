#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Node:
    def __init__(self,val):
        """
        minimalistic defintion of a Node object
        each node of the tree is defined by a value
        navigation through the tree structure is done by accessing the left or right
        child of the node
        """
        self.val = val
        self.left = self.right = None
