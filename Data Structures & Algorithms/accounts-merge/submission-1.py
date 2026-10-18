from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj = defaultdict(set)
        emailToName = {}
        for account in accounts:
            name = account[0]
            emails = account[1:]
            for email1 in emails:
                adj[email1].add(emails[0])
                adj[emails[0]].add(email1)
                emailToName[email1] = name

        seen = set()
        res = []

        def dfs(email, comp):
            if email in seen:
                return
            
            seen.add(email)
            comp.append(email)
            nei = adj[email]
            for n in nei:
                dfs(n, comp)


        for email, nei in adj.items():
            if email in seen:
                continue
            comp = []
            dfs(email, comp)
            res.append([emailToName[email]] + sorted(comp))
        
        return res
        

        