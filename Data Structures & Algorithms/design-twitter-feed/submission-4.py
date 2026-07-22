class Twitter:

    def __init__(self):
        self.followees = collections.defaultdict(set)
        self.tweets = collections.defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = self.followees[userId] | {userId}
        for u in users:
            if u in self.tweets:
                ind = len(self.tweets[u]) - 1
                time, val = self.tweets[u][ind]
                heap.append( (time, val, u, ind-1))
        
        heapq.heapify(heap)
        res = []
        while heap and len(res) < 10:
            print(heap)
            time, val, user, ind = heapq.heappop(heap)
            res.append(val)
            print(res)
            if ind >= 0:
                t, v = self.tweets[user][ind]
                heapq.heappush(heap, (t, v, user, ind-1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)
