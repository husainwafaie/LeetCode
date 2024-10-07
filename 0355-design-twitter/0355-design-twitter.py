class Twitter:

    def __init__(self):
        self.users = {}
        self.time = 0
        self.dct = {}

    def _add(self, userId: int):
        self.users[userId] = [set(), [], set()]
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self._add(userId)
            heapq.heappush(self.users[userId][1], (self.time, tweetId))
            self.users[userId][2].add((self.time, tweetId))
            self.dct[tweetId] = self.time
            self.time += 1
            return
        self.dct[tweetId] = self.time
        heapq.heappush(self.users[userId][1], (self.time, tweetId))
        self.users[userId][2].add((self.time, tweetId))
        for i in self.users[userId][0]:
            heapq.heappush(self.users[i][1], (self.time, tweetId))
        self.time += 1
         
    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            return
        return [i[1] for i in heapq.nlargest(10, self.users[userId][1])]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followeeId in self.users and followerId in self.users[followeeId][0]:
            return
        if followeeId not in self.users:
            self._add(followeeId)
        if followerId not in self.users:
            self._add(followerId)
        self.users[followeeId][0].add(followerId)
        for i in self.users[followeeId][2]:
            heapq.heappush(self.users[followerId][1], i)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followeeId not in self.users:
            self._add(followeeId)
        if followerId not in self.users:
            self._add(followerId)
        if followerId not in self.users[followeeId][0]:
            return
        self.users[followeeId][0].remove(followerId)
        for i in self.users[followeeId][2]:
            self.users[followerId][1].remove(i)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)