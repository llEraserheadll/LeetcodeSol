class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        min_heap = []

        for j in range(1,len(arr)):
            min_heap.append((arr[0]/arr[j],0,j))
        heapify(min_heap)

        for _ in range(k - 1):
            val,i,j = heappop(min_heap)

            if i + 1< j:
                heappush(min_heap,(arr[i+1] / arr[j],i+1,j))
        
        value,i,j = heappop(min_heap)

        return [arr[i],arr[j]]