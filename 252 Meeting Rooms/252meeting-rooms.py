class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
    
        min_heap = []

        intervals.sort(key = lambda x:x[0])

        for start_time,end_time in intervals:
            if min_heap and start_time < min_heap[0]:
                return False
            
            while min_heap and start_time >= min_heap[0]:
                heappop(min_heap)
            
            heappush(min_heap,end_time)

        return True

        