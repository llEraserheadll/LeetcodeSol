def quickselect(nums,k):
    left,right,mid = [],[],[]
    pivot = random.choice(nums)

    for num in nums:
        if num > pivot:
            left.append(num)
        elif num < pivot:
            right.append(num)
        else:
            mid.append(num)
    
    if k <= len(left):
        return quickselect(left,k)

    if k > len(left) + len(mid):
        return quickselect(right,k - len(left) - len(mid))
    
    return pivot


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return quickselect(nums,k)
        