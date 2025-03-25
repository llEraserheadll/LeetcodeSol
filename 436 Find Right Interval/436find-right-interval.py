from heapq import *
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_heap = []
        end_heap = []
        result = [-1]*len(intervals)

        for i in range(len(intervals)):
            heappush(start_heap,(intervals[i][0],i))
            heappush(end_heap,(intervals[i][1],i))

        while end_heap:
            value,index = heappop(end_heap)

            while start_heap and start_heap[0][0] < value:
                heappop(start_heap)
            
            if start_heap:
                result[index] = start_heap[0][1]
        
        return result



        