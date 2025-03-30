from heapq import heappush, heappop
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for x,y in points:
            dist = x**2 + y**2
            if len(max_heap) < k:
                heappush(max_heap,(-dist,x,y))
            elif -dist > max_heap[0][0]:
                heappop(max_heap)
                heappush(max_heap,(-dist,x,y))
        return [[x,y] for _,x,y in max_heap]