def quickselect(nums,k):
    pivot = random.choice(nums)
    left,right,mid = [],[],[]    
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
    def thirdMax(self, nums: List[int]) -> int:

        d_num = list(set(nums))
        if len(d_num) == 1:
            return d_num[0]
        elif len(d_num) < 3:
            return max(d_num[0],d_num[1])
        return quickselect(d_num,3)