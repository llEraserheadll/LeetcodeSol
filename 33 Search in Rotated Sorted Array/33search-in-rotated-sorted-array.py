def binary_search(nums,left,right,target):
    if left > right:
        return -1
    mid = left + ((right - left)//2)

    if nums[mid] == target:
        return mid
    
    if nums[left] <= nums[mid]:
        if target >= nums[left] and target < nums[mid]:
            return binary_search(nums,left,mid-1,target)
        else:
            return binary_search(nums,mid+1,right,target)
    else:
        if target > nums[mid] and target <= nums[right]:
            return binary_search(nums,mid+1,right,target)
        else:
            return binary_search(nums,left,mid-1,target)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        return binary_search(nums,left,right,target)
        