from heapq import heappush,heappop
class Solution:
    def reorganizeString(self, s: str) -> str:
        char_counter = {}

        for char in s:
            if char in char_counter:
                char_counter[char] += 1
            else:
                char_counter[char] = 1
        
        previous = None
        result = ""
        max_heap = []
        for char,count in char_counter.items():
            max_heap.append([-count,char])
        
        heapify(max_heap)

        while max_heap or previous:

            if previous and len(max_heap) == 0:
                return ""
            
            count,char = heappop(max_heap)
            result = result + char
            count += 1

            if previous:
                heappush(max_heap,previous)
                previous = None
            
            if count != 0:
                previous = [count,char]
        
        return result

        