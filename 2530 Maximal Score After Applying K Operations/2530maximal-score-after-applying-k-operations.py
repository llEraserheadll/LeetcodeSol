from heapq import heappush,heappop
import math
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]
        heapify(max_heap)
        result = 0

        for _ in range(k):
            value = -heappop(max_heap)
            result += value

            heappush(max_heap,-math.ceil(value / 3))
        
        return result
