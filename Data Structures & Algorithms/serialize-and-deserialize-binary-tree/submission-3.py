# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        q = deque([root])

        while q:
            cur = q.popleft()
            if not cur:
                res.append('N')
            else:
                res.append(str(cur.val))
                q.append(cur.left)
                q.append(cur.right)
        
        return ' '.join(res)
        
        # res = []

        # def dfs(node):
        #     if not node:
        #         res.append('N')
        #         return
            
        #     res.append(str(node.val))
        #     dfs(node.left)
        #     dfs(node.right)

        # dfs(root)
        # return ' '.join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(' ')
        if nodes[0] == 'N':
            return None

        root = TreeNode(nodes[0])
        q = deque([root])
        
        i = 1
        while q:
            cur = q.popleft()
            if not cur:
                continue
            left = TreeNode(nodes[i]) if nodes[i] != 'N' else None
            right = TreeNode(nodes[i+1]) if nodes[i+1] != 'N' else None
            i += 2
            cur.left = left
            cur.right = right
            q.append(left) 
            q.append(right)
        
        return root




        
        
        # nodes = data.split(' ')
        # i = 0

        # def dfs():
        #     nonlocal i

        #     if nodes[i] == 'N':
        #         i += 1
        #         return None

        #     cur = TreeNode(nodes[i])
        #     i += 1

        #     cur.left = dfs()
        #     cur.right = dfs()
        #     return cur
        
        # return dfs()
            




