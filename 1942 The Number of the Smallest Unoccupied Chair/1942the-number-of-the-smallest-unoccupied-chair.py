from heapq import heappush,heappop
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        used_chair = []
        available_chair = []
        sorted_friends = sorted(enumerate(times),key = lambda x:x[1][0])
        chair_index = 0

        for friend_index,(arrival,departure) in sorted_friends:
            while used_chair and used_chair[0][0] <= arrival:
                _,chair = heappop(used_chair)
                heappush(available_chair,chair)
            
            if available_chair:
                new_chair = heappop(available_chair)
            else:
                new_chair = chair_index
                chair_index += 1
            
            heappush(used_chair,(departure,new_chair))

            if friend_index == targetFriend:
                return new_chair