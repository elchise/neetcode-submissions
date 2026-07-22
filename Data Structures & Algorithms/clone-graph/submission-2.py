"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        oldToNew = {}

        q = deque()
        q.append(node)
        oldToNew[node] = Node(node.val)

        while q:
            cur = q.popleft()
            for n in cur.neighbors:
                if n not in oldToNew:
                    q.append(n)
                    oldToNew[n] = Node(n.val)
            
                oldToNew[cur].neighbors.append(oldToNew[n])
                
        return oldToNew[node]



        # def dfs(n):
        #     if n in oldToNew:
        #         return oldToNew[n]
            
        #     cur = Node(n.val, [])
        #     oldToNew[n] = cur

        #     for neigh in n.neighbors:
        #         cur.neighbors.append(dfs(neigh))
            
        #     return cur
                
        # return dfs(node) if node else None



