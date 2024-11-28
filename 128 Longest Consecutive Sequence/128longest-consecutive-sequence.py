class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))

        max_length = 0
        n = len(nums)
        j = 0
        
        while j < n:
            start = j
            while j+1 < n and nums[j] == nums[j+1] - 1:
                j += 1
            max_length = max(max_length, j-start+1)
            if j == start: j += 1
            

        return max_length

