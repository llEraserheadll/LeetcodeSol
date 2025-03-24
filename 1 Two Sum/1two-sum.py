class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            search = target - nums[i]
            if search in nums and i != nums.index(search):
                return [i, nums.index(search)]
            
            




