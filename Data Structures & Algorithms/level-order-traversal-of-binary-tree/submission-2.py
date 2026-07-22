# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque()
        if not root:
            return res

        q.append((0, root))
        curLevel = []
        level = 0

        while q:
            l, n = q.popleft()
            if l != level:
                res.append(curLevel)
                level += 1
                curLevel = []

            if n:
                curLevel.append(n.val)
                # if n.left is not None:
                q.append((level+1, n.left))
                # if n.left is not None:
                q.append((level+1, n.right))

        # res.append(curLevel)
            
        return res
