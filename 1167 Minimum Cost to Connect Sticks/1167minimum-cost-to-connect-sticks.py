from heapq import *
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        total_cost = 0

        while len(sticks) > 1:
            first = heappop(sticks)
            second = heappop(sticks)

            cost = first + second
            total_cost += cost

            heappush(sticks,cost)

        return total_cost
        
