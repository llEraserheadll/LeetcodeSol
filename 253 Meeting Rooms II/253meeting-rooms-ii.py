import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x:x[0])
        min_heap = []
        

        for start_time,end_time in intervals:

            if min_heap and start_time >= min_heap[0]:
                heapq.heappop(min_heap)
            
            heapq.heappush(min_heap,end_time)
        
        return len(min_heap)


        