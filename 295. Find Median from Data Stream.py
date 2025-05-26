class MedianFinder:

    def __init__(self):
        self.small,self.large=[],[]
        

    def addNum(self, num: int) -> None:

        #Add the num in the max-heap by default 
        heapq.heappush(self.small, -1*(num))
        #handle the case where unequal heaps and if values are added in the wrong way 
        if((self.small and self.large) and self.large[0]< (-1)*self.small[0]):
            val=-heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large) >len(self.small)+1:
            val=heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)

        if len(self.small)>len(self.large)+1:
            val=-heapq.heappop(self.small)
            heapq.heappush(self.large,val)


        

    def findMedian(self) -> float:
        if len(self.small)>len(self.large):
            return self.small[0]*(-1)
        elif len(self.small)<len(self.large):
            return self.large[0]
        return (self.large[0]+self.small[0]*(-1))/2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
