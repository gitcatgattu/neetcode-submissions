class Twitter:

    def __init__(self):
        self.users={}
        self.feed=[]
        heapq.heapify(self.feed)
        self.time=-1

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId]=set([userId])
        heapq.heappush(self.feed,[self.time,userId,tweetId])
        self.time-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        removedFeed=[]
        res=[]
        i=1
        while self.feed and i<=10:
            feed=heapq.heappop(self.feed)
            removedFeed.append(feed)
            if feed[1] in self.users[userId]:
                res.append(feed[2])
                i+=1
        while removedFeed:
            heapq.heappush(self.feed,removedFeed.pop())
            
        return res








    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId]=set([followerId])
        if followeeId not in self.users:
            self.users[followeeId]=set([followeeId])
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId] and followerId!=followeeId:
            self.users[followerId].remove(followeeId)
