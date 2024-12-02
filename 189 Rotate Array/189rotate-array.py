class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # k = k % n
        # rotate = [0]*n

        # for i in range(n):
        #     rotate[(i + k) % n] = nums[i]
        
        # for i in range(n):
        #     nums[i] = rotate[i]

        n = len(nums)
        k = k % n

        def reverse(left,right):
            while left < right:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
                right -= 1
        
        reverse(0,len(nums) - 1)
        reverse(0,k-1)
        reverse(k,len(nums) -1)
