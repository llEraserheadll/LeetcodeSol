class MedianFinder:

    def __init__(self):
        self.min_heap_largenum = []
        self.max_heap_smallnum = []
        

    def addNum(self, num: int) -> None:

        if not self.max_heap_smallnum or -self.max_heap_smallnum[0] >= num:
            heappush(self.max_heap_smallnum , -num)
        else:
            heappush(self.min_heap_largenum , num)
        
        if len(self.max_heap_smallnum) > len(self.min_heap_largenum) + 1:
            heappush(self.min_heap_largenum,-heappop(self.max_heap_smallnum))
        elif len(self.min_heap_largenum) > len(self.max_heap_smallnum):
            heappush(self.max_heap_smallnum,-heappop(self.min_heap_largenum))
        

    def findMedian(self) -> float:
        if len(self.max_heap_smallnum) == len(self.min_heap_largenum):
            return -self.max_heap_smallnum[0] / 2.0 + self.min_heap_largenum[0] / 2.0
        return -self.max_heap_smallnum[0] / 1.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()