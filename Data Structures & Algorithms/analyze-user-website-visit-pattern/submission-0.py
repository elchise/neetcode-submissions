class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        mp = defaultdict(list)
        for t, user, web in sorted(zip(timestamp, username, website)):
            mp[user].append(web)
        
        count = defaultdict(int)
        for user in mp:
            patterns = set()
            websites = mp[user]
            for i in range(len(websites)):
                for j in range(i + 1, len(websites)):
                    for k in range(j + 1, len(websites)):
                        patterns.add((websites[i], websites[j], websites[k]))
            
            for p in patterns:
                count[p] += 1
        
        res = None
        maxCount = 0
        for pattern, c in count.items():
            if c > maxCount or (c == maxCount and pattern < res):
                res = pattern
                maxCount = c

        return list(res) 
