from heapq import *
class Solution:
    def largestInteger(self, num: int) -> int:
        even_heap = []
        odd_heap = []
        digits = [int(d) for d in str(num)]
        result = []

        for d in digits:
            if d % 2 == 0:
                heappush(even_heap,-d)
            else:
                heappush(odd_heap,-d)
        
        for d in digits:
            if d % 2 ==0:
                even = -heappop(even_heap)
                result.append(even)
            else:
                odd =  -heappop(odd_heap)
                result.append(odd)
        
        return int(''.join(map(str,result)))
        