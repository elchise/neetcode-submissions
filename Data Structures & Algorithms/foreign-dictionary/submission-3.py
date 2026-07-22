class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}
        indegree = {c: 0 for c in adj}
        for i in range(0, len(words)-1):
            cur, nxt = words[i], words[i+1]
            j = 0
            while cur[j] == nxt[j]:
                j += 1
                if j >= len(cur):
                    break
                if j >= len(nxt):
                    return ""
            if j >= len(cur):
                    continue
            if nxt[j] not in adj[cur[j]]:
                adj[cur[j]].add(nxt[j])
                indegree[nxt[j]] += 1
        
        q = deque()
        print(indegree, adj)
        for c in indegree:
            if indegree[c] == 0:
                q.append(c)
        
        res = []
        while q:
            c = q.popleft()
            res.append(c)
            for nxt in adj[c]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        
        if len(res) != len(indegree):
            return ""

        return "".join(res)


