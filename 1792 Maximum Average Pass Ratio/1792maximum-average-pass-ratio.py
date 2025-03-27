from heapq import heappush,heappop,heapify
def gain(passes,total):
    return (float(passes + 1)/(total + 1)) - (float(passes)/total)

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        max_heap = []
        for passes,total in classes:
            gain1 = gain(passes,total)
            max_heap.append((-gain1,passes,total))
        
        heapify(max_heap)
        
        for _ in range(extraStudents):
            current_gain,passes,total = heappop(max_heap)
            passes += 1
            total += 1
            heappush(max_heap,(-gain(passes,total),passes,total))
        
        total_ratio = sum(float(passes)/total for _,passes,total in max_heap)

        ratio = total_ratio / len(classes)
    
        return ratio
        
        