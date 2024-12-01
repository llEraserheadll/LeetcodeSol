class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # count = 0
        # candidate = 0

        # for num in nums:
        #     if count == 0:
        #         candidate = num

        #     if num == candidate:
        #         count += 1
        #     else:
        #         count -= 1
        
        # return candidate

        n=len(nums)
        m = defaultdict(int)

        for num in nums:
            m[num] += 1
        
        n = n // 2

        for key,value in m.items():
            if value > n:
                return key
        
        return 0