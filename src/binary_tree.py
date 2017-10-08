import random


class Node:
    def __init__(self,val):
        self.val = val
        self.left = self.right = None


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
        pass

    def visualize(self):
        """
        tree-like representation of the tree structure
        """
        pass

    def asList(self):
        """
        returns list of tuples, each containing the node value and an integer value indicating the level
        (eg. if self.root is set to 3 the first item of the list should be (3,0)).
        """
        pass

    def getLCA(self, node1, node2):
        """
        returns LCA of node1 and nod2
        """
        pass

"""
if __name__=="__main__":
    n1 = Node(3)
    bt = BinaryTree()
    bt.insertNode(n1)
"""
