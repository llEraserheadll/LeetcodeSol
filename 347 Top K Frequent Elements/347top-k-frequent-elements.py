from collections import Counter
import random

def quickselect(arr,left,right,k):

    if left == right:
        return
    
    pivot_index = random.randint(left,right)
    pivot_index = partition(arr,left,right,pivot_index)

    if k > pivot_index:
        quickselect(arr,pivot_index + 1,right,k)
    elif k < pivot_index:
        quickselect(arr,left,pivot_index-1,k)

def partition(arr,left,right,pivot_index):
    pivot_frequency = arr[pivot_index][1]
    arr[pivot_index],arr[right] = arr[right],arr[pivot_index]
    store_index = left

    for i in range(left,right):
        if arr[i][1] > pivot_frequency:
            arr[store_index],arr[i] = arr[i],arr[store_index]
            store_index += 1
    
    arr[store_index],arr[right] = arr[right],arr[store_index]

    return store_index


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # number_count = {}
        # max_heap = []
        # result = []

        # for numbers in nums:
        #     if numbers in number_count:
        #         number_count[numbers] += 1
        #     else:
        #         number_count[numbers] = 1
        
        # for number,count in number_count.items():
        #     heappush(max_heap,(-count,number))
        
        # for i in range(k):
        #     _,value = heappop(max_heap)
        #     result.append(value)
        
        # return result



        number_count  = Counter(nums)
        array = list(number_count.items())

        quickselect(array,0,len(array)-1,k-1)

        return [array[i][0] for i in range(k)]
