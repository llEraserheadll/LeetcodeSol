class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        def next_step(pointer,value,size):
            return (pointer+value)% size

        def valid_loop(prev_direction,nums,pointer):
            curr_direction = nums[pointer] > 0

            if curr_direction != prev_direction or nums[pointer] % len(nums) == 0:
                return True
            else:
                return False

                
        size = len(nums)
        for i in range(size):
            slow = fast = i

            prev_direction = nums[i] > 0

            while True:
                slow = next_step(slow,nums[slow],size)
                if valid_loop(prev_direction,nums,slow):
                    break

                fast = next_step(fast,nums[fast],size)
                if valid_loop(prev_direction,nums,fast):
                    break
                
                fast = next_step(fast,nums[fast],size)
                if valid_loop(prev_direction,nums,fast):
                    break
                

                if slow == fast:
                    return True
        return False
    





        