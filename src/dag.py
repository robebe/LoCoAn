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
                #self.size += 1

    def asList(self):
        return list(self.graph.items())

    def getLCA2(self, val1, val2):
        ret = []
        frst, scnd = self._insertionOrder(val1, val2)
        #scnd is direct child of frst
        if scnd in self.graph[frst]:
            return [frst]
        for key, vals in self.graph.items():
            #shared parent node
            if frst in vals and scnd in vals:
                ret.append(key)
        return ret

    def getLCA(self, val1, val2):
        return list(set(self._dagLCA(val1, val2)))

    def _dagLCA(self, val1, val2, ret=[]):
        if val1 in self.graph[val2]:
            ret.append(val2)
        elif val2 in self.graph[val1]:
            ret.append(val1)
        else:
            for key, vals in self.graph.items():
                if val1 and val2 in vals:
                    ret = [key for key, vals in self.graph.items() if val1 in vals and val2 in vals]
                    break
                elif val1 in vals:
                    val1 = key
                    self._dagLCA(val1, val2, ret)
                elif val2 in vals:
                    val2 = key
                    self._dagLCA(val1, val2, ret)
        return ret
