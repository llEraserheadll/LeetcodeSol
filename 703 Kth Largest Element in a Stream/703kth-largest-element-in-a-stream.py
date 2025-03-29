from heapq import heappush,heappop
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k

        for elements in nums:
            self.add(elements)
        

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heappush(self.min_heap,val)
        elif val > self.min_heap[0]:
            heappop(self.min_heap)
            heappush(self.min_heap,val)
        
        return self.min_heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)