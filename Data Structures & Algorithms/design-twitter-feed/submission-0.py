class Twitter:

    def __init__(self):
        self.followers = {}
        self.tweets = {}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        all = self.followers.get(userId, set()).copy()
        all.add(userId)
        heap = []
        heapq.heapify(heap)
        for i in all:
            if i not in self.tweets:
                continue
            num = len(self.tweets[i]) - 1
            for j in range(num, max(-1, num - 10), -1):
                (time, tid) = self.tweets[i][j]
                heapq.heappush(heap, (time, tid))
                if len(heap) > 10:
                    heapq.heappop(heap)
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set()
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            self.followers[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)