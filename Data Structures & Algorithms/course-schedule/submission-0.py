from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        numPrereqs = [0]*numCourses
        prereqs = collections.defaultdict(list)
        count = 0
        for a, b in prerequisites:
            numPrereqs[a]+=1
            prereqs[b].append(a)
        
        q = deque()
        for i in range(numCourses):
            if numPrereqs[i] == 0:
                q.append(i)

        while q:
            cur = q.popleft()
            count+=1
            for i in prereqs[cur]:
                numPrereqs[i]-=1
                if numPrereqs[i] == 0:
                    q.append(i)
        
        print(count)
        return count == numCourses
                
            