from heapq import heappush,heappop
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = []

        for i in range(len(quality)):
            workers.append((wage[i]/quality[i],quality[i]))
        
        workers.sort(key = lambda x:x[0])
        max_heap = []
        min_cost = float('inf')
        total_quality = 0

        for ratio,q in workers:
            heappush(max_heap,-q)
            total_quality += q

            if len(max_heap) > k:
                remove_q = -heappop(max_heap)
                total_quality -= remove_q
            
            if len(max_heap) == k:
                min_cost = min(min_cost,ratio * total_quality)
        
        return min_cost