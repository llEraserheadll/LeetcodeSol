import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        current_capital = w
        capital_min_heap = []
        profits_max_heap = []
        

        for x in range(len(capital)):
            heapq.heappush(capital_min_heap,(capital[x],x))
        
        for _ in range(k):

            while capital_min_heap and capital_min_heap[0][0] <= current_capital:
                c,i = heapq.heappop(capital_min_heap)
                heapq.heappush(profits_max_heap,(-profits[i]))
            
            if not profits_max_heap:
                break
            
            j = - heapq.heappop(profits_max_heap)
            current_capital = current_capital + j
        
        return current_capital


        