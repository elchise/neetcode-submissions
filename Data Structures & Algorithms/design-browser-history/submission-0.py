class BrowserHistory:

    def __init__(self, homepage: str):
        self.visited = [homepage]
        self.cur = 0
        self.last = self.cur

    def visit(self, url: str) -> None:
        self.cur += 1
        self.last = self.cur
        if self.cur < len(self.visited):
            self.visited[self.cur] = url
        else:
            self.visited.append(url)        

    def back(self, steps: int) -> str:
        toVisit = max(0, self.cur - steps)
        self.cur = toVisit
        return self.visited[self.cur]

    def forward(self, steps: int) -> str:
        toVisit = min(self.last, self.cur + steps)
        self.cur = toVisit
        return self.visited[self.cur]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)