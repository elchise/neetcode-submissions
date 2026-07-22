class Twitter:

    def __init__(self):
        self.followees = collections.defaultdict(set)
        self.tweets = collections.defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        print(self.tweets)
        for f in self.followees[userId]:
            t = self.tweets[f]
            if len(self.tweets[f]) < 10:
                feed.extend(self.tweets[f])
            else:
                feed.extend(t[len(t)-10:])
        if userId not in self.followees[userId]:
            feed.extend(self.tweets[userId])
        print(feed)
        heapq.heapify(feed)
        res = [] 
        while feed and len(res) < 10:
            res.append(heapq.heappop(feed)[1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)
