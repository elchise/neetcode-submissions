from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0]*numCourses
        adj  = collections.defaultdict(list)
        order = []
        # q = deque()

        for a, b in prerequisites:
            adj[b].append(a)
            inDegree[a]+=1
        
        # for i in range(numCourses):
        #     if inDegree[i] == 0:
        #         q.append(i)
        
        # while q:
        #     cur = q.popleft()
        #     order.append(cur)

        #     for nextCourse in adj[cur]:
        #         inDegree[nextCourse]-=1
        #         if inDegree[nextCourse] == 0:
        #             q.append(nextCourse)
        
        # if len(order) == numCourses:
        #     return order
         
        # return []

        res = []
        completed = set()
        def dfs(node):
            res.append(node)
            completed.add(node)
            for i in adj[node]:
                inDegree[i] -= 1
                if inDegree[i] == 0:
                    dfs(i)

        for i in range(numCourses):
            if inDegree[i] == 0 and i not in completed:
                dfs(i)
        
        if len(res) >= numCourses:
            return res
        
        return []

