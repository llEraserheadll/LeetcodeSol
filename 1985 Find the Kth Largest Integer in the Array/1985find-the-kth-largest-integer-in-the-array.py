def quickselect(arr,k):
    pivot = random.choice(arr)
    left,mid,right = [],[],[]

    for val in arr:
        if val > pivot:
            left.append(val)
        elif val < pivot:
            right.append(val)
        else:
            mid.append(val)
    
    if k <= len(left):
        return quickselect(left,k)
    
    if k > len(left) + len(mid):
        return quickselect(right,k-len(left)-len(mid))

    return str(pivot)

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        new_num = list(map(int,nums))
        return quickselect(new_num,k)
        