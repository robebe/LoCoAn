#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from collections import OrderedDict


class DirectedAcyclicGraph:

    def __init__(self, root_val=1):
        self.graph = OrderedDict()
        self.graph[root_val] = []
        self.size = 1

    def add_root_node(self, val, child_val):
        #child value is existent in graph
        if child_val in [key for key in self.graph.keys()]:
            #has to be non existend value
            if not val in self.graph.keys():
                #no links both to and from the nodes
                #if not val in self.graph[child_val]:
                self.graph[val] = [child_val]
                self.size += 1

    def add_node(self, val, parent_val):
        if parent_val in self.graph.keys():
            #add new node
            if not val in self.graph.keys():
                self.graph[parent_val].append(val)
                self.graph[val] = []
                self.size += 1
            #add edge to existing node pair
            elif not parent_val in self.graph[val] and not val in self.graph[parent_val]:
            #make sure both nodes are not connected via a child node (false assumption!!)
            #if len([child for child in self.graph[parent_val] if child in self.graph[val]]) == 0:
                self.graph[parent_val].append(val)
                self.size += 1

    def asList(self):
        return list(self.graph.items())

    def getLCA(self, val1, val2):
        pass
