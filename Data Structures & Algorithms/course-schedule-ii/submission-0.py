from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0]*numCourses
        adj = collections.defaultdict(list)
        order = []
        q = deque()

        for a, b in prerequisites:
            adj[b].append(a)
            inDegree[a]+=1
        
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        
        while q:
            cur = q.popleft()
            order.append(cur)

            for nextCourse in adj[cur]:
                inDegree[nextCourse]-=1
                if inDegree[nextCourse] == 0:
                    q.append(nextCourse)
        
        if len(order) == numCourses:
            return order
         
        return []

