class Solution:
    def cleanup(self,i,current_window,nums):
        while current_window and nums[i] >= nums[current_window[-1]]:
            current_window.pop()

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        
        output = []
        current_window = deque()

        for i in range(k):
            self.cleanup(i , current_window , nums)
            current_window.append(i)
        output.append(nums[current_window[0]])

        for i in range(k,len(nums)):
            self.cleanup(i,current_window,nums)
            if current_window and current_window[0] <= (i - k):
                current_window.popleft()
            current_window.append(i)
            output.append(nums[current_window[0]])
        return output

        