from heapq import heapify,heappush,heappop
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        min_heap = []
        heappush(min_heap,(2,2,0))
        heappush(min_heap,(3,3,0))
        heappush(min_heap,(5,5,0))

        ugly = [1]

        while len(ugly) < n:
            ugly_num,prime,index = heappop(min_heap)

            if ugly_num != ugly[-1]:
                ugly.append(ugly_num)
            
            heappush(min_heap,(prime * ugly[index+1],prime,index+1))
        
        return ugly[-1]
