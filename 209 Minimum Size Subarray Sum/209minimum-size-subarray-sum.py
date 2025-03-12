class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        substr_len = float('inf')
        length = 0
        sum = 0

        for right in range(len(nums)):
            sum += nums[right]
            while sum >= target:
                length = (right + 1) - left
                substr_len = min(substr_len,length)
                sum -= nums[left]
                left += 1
        
        if substr_len != float('inf'):
            return substr_len
        
        return 0