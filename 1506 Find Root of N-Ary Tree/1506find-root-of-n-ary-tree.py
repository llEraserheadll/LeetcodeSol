"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        par = sum([i.val for i in tree])
        child = sum([k.val for j in tree for k in j.children])
        root = par - child
        
        return [i for i in tree if i.val == root][0]