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

    def getLCA(self, val1, val2):
        self.lca_list = []
        self._dagLCA(val1, val2)
        ret = list(set(self.lca_list))
        if len(ret) > 1:
            last_found = ret[-1]
            last_vals = self.graph[last_found]
            ret = [key for key, vals in self.graph.items() if vals == last_vals]
        return ret

    def _dagLCA(self, val1, val2):
        for key in reversed(list(self.graph.keys())):
            vals = self.graph[key]
            if val1 in self.graph[val2]:
                self.lca_list.append(val2)
            elif val2 in self.graph[val1]:
                self.lca_list.append(val1)
            elif val1 in vals and val2 in vals:
                tmp =  [key for key, vals in self.graph.items() if val1 in vals and val2 in vals]
                for t in tmp:
                    self.lca_list.append(t)
            elif val2 in vals:
                search_for = [key for key, vals in self.graph.items() if val2 in vals]
                for val2 in search_for:
                    self._dagLCA(val1, val2)
            elif val1 in vals:
                search_for = [key for key, vals in self.graph.items() if val1 in vals]
                for val1 in search_for:
                    self._dagLCA(val1, val2)
