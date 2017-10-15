#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from binary_tree import BinaryTree
import random


def main():
    """
    show functionality of LoCoAn
    """
    bt = BinaryTree()
    numbers = [random.randint(0,100) for i in range(20)]
    print("Randomly generated list of numbers to be inserted:\n", numbers)
    [bt.insertNode(num) for num in numbers]
    print("\nResulting tree structure:")
    for node in bt.visualize():
        print(node)
    indexes = [(random.randint(0,len(numbers)-1),random.randint(0, len(numbers)-1)) for i in range(5)]
    print("\nTree as list of (value, level)-tuples:")
    print(bt.asList())
    print("\nSome example values for Lowest Common Ancestor:")
    for i,j in indexes:
        print(bt.getLCA(numbers[i], numbers[j], visualize=True))



if __name__=="__main__":
    main()
