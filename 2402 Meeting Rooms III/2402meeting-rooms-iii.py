class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        used_rooms = []
        available = []
        for i in range(n):
            available.append(i)
        
        count = [0]*n

        meetings.sort(key = lambda x:x[0])

        for start_time,end_time in meetings:

            while used_rooms and used_rooms[0][0] <= start_time:
                _,rooms = heappop(used_rooms)
                heappush(available,rooms)
            
            if not available:
                end,rooms = heappop(used_rooms)
                end_time = end + (end_time - start_time)
                heappush(available,rooms)
            
            rooms = heappop(available)
            heappush(used_rooms,(end_time,rooms))
            count[rooms] += 1
        return count.index(max(count))
        