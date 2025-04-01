class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        min_heap = []

        for i,num in enumerate(nums):
            heappush(min_heap,(num,i))

            if len(min_heap) > k:
                heappop(min_heap)
        
        sorted_num = sorted(min_heap,key = lambda x:x[1])

        return [x[0] for x in sorted_num]