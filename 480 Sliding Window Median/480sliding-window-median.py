class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        outgoing_nums = {}
        medians = []
        max_heap = []
        min_heap = []
        balance = 0
        j = k

        for i in range(0,k):
            heappush(max_heap,-nums[i])
        
        for i in range(0,k // 2):
            heappush(min_heap,-max_heap[0])
            heappop(max_heap)
        
        while True:

            if k % 2 == 0:
                medians.append((float(-max_heap[0])+ float(min_heap[0]))* 0.5)
            else:
                medians.append(float(-max_heap[0]))

            if j >= len(nums):
                break
            
            out_num = nums[j - k]
            inc_num = nums[j]
            j += 1

            if out_num <= -max_heap[0]:
                balance -= 1
            else:
                balance += 1
            
            if out_num in outgoing_nums:
                outgoing_nums[out_num] += 1
            else:
                outgoing_nums[out_num] = 1
            
            if max_heap and inc_num <= -max_heap[0]:
                balance += 1
                heappush(max_heap,-inc_num)
            else:
                balance -= 1
                heappush(min_heap,inc_num)
            
            if balance > 0:
                heappush(min_heap,-max_heap[0])
                heappop(max_heap)
            elif balance < 0 : 
                heappush(max_heap,-min_heap[0])
                heappop(min_heap)
            
            balance = 0

            while -max_heap[0] in outgoing_nums and outgoing_nums[-max_heap[0]] > 0:
                outgoing_nums[-max_heap[0]] = outgoing_nums[-max_heap[0]] - 1
                heappop(max_heap)
            
            while min_heap and min_heap[0] in outgoing_nums and outgoing_nums[min_heap[0]] > 0:
                outgoing_nums[min_heap[0]] = outgoing_nums[min_heap[0]] - 1
                heappop(min_heap)
            
        return medians    

