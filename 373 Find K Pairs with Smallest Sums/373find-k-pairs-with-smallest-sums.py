class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        min_heap = []
        result = []
        counter = 1

        for i in range(min(k,len(nums1))):
            heappush(min_heap,(nums1[i]+nums2[0],i,0))
        
        while min_heap and counter <= k:
            sum,i,j = heappop(min_heap)
            result.append([nums1[i],nums2[j]])

            if j + 1<len(nums2):
                heappush(min_heap,(nums1[i]+nums2[j+1],i,j+1))
            
            counter += 1
        return result
        