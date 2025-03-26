from heapq import heapify,heappush,heappop
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        min_heap = []
        min_heap = [(prime,prime,0) for prime in primes]
        heapify(min_heap)
        ugly = [1]

        while len(ugly) < n:
            ugly_num,prime,index = heappop(min_heap)

            if ugly_num != ugly[-1]:
                ugly.append(ugly_num)
            
            heappush(min_heap,(prime*ugly[index+1],prime,index+1))
        
        return ugly[-1]
        