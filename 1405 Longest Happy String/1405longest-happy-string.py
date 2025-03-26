from heapq import heappush,heappop
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        result = []

        if a > 0:
            heappush(max_heap,(-a,"a"))
        if b > 0:
            heappush(max_heap,(-b,"b"))
        if c > 0:
            heappush(max_heap,(-c,"c"))

        while max_heap:
            count,character = heappop(max_heap)
            count = -count

            if(len(result) >= 2 and result[-1] == character and result[-2] == character):
                if not max_heap:
                    break
                tmpcount,tmpchar = heappop(max_heap)
                tmpcount = -tmpcount
                tmpcount -= 1
                result.append(tmpchar)
                if tmpcount > 0:
                    heappush(max_heap,(-tmpcount,tmpchar))
                heappush(max_heap,(-count,character))
            else:
                count -= 1
                result.append(character)
                if count > 0:
                    heappush(max_heap,(-count,character))
        return ''.join(result)

        