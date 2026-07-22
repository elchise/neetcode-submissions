from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        numPrereqs = [0]*numCourses
        prereqs = collections.defaultdict(list)
        count = 0
        for a, b in prerequisites:
            numPrereqs[a]+=1
            prereqs[b].append(a)
        
        # q = deque()
        # for i in range(numCourses):
        #     if numPrereqs[i] == 0:
        #         q.append(i)

        # while q:
        #     cur = q.popleft()
        #     count+=1
        #     for i in prereqs[cur]:
        #         numPrereqs[i]-=1
        #         if numPrereqs[i] == 0:
        #             q.append(i)

        visited = set()
        def dfs(node):
            if node in visited:
                return False
            if len(prereqs[node]) == 0:
                return True
            
            visited.add(node)
            for i in prereqs[node]:
                if not dfs(i):
                    return False
            visited.remove(node)
            prereqs[node] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
        # return count == numCourses
                
            