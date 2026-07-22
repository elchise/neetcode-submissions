"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not Node:
            return

        newNodes = {}
        def dfs(n):
            if n is None:
                return
            if n in newNodes:
                return newNodes[n]
            nei = n.neighbors
            newNode = Node(n.val)
            newNodes[n] = newNode

            for ne in nei:
                newNode.neighbors.append(dfs(ne))
            return newNode
        
        return dfs(node)
                



        
