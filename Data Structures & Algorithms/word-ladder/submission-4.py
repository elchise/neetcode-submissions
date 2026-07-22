from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # if endWord not in wordList or beginWord == endWord:
        #     return 0

        words = set(wordList)
        if beginWord == endWord or endWord not in wordList:
            return 0

        res = 0
        q = deque([beginWord])
        visited = set()
        while q:
            res += 1
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == endWord:
                    return res
                
                for i in range(len(cur)):
                    for c in range(97, 97+26):
                        if chr(c) == cur[i]:
                            continue
                        w = cur[:i] + chr(c) + cur[i+1:]
                        if w in words and w not in visited:
                            visited.add(w)
                            q.append(w)

            
        
        return 0