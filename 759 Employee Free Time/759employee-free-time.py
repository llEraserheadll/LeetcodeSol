"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        result = []
        heap = []

        for i in range(len(schedule)):
            heap.append((schedule[i][0].start,i,0))
        
        heapq.heapify(heap)

        previous = schedule[heap[0][1]][heap[0][2]].start

        while heap:
            _,i,j  = heapq.heappop(heap)
            interval = schedule[i][j]

            if interval.start > previous:
                result.append(Interval(previous,interval.start))
            
            previous = max(previous,interval.end)
            
            if j + 1 < len(schedule[i]):
                heapq.heappush(heap,(schedule[i][j+1].start,i,j+1))
        
        return result
        