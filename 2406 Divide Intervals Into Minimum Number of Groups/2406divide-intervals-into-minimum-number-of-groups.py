from heapq import heappush,heappop
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        max_count = 0
        min_heap = []

        for start,end in intervals:
            while min_heap and min_heap[0] < start:
                heappop(min_heap)
            
            heappush(min_heap,end)

            max_count = max(max_count,len(min_heap))
        
        return max_count