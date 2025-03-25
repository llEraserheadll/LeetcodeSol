class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

       min_heap = []
       matrix_length = len(matrix)

       for i in range(matrix_length):
            if len(matrix[i]) == 0:
                continue
            else:
                heappush(min_heap,(matrix[i][0],i,0))
       
       counter = 0

       while min_heap:
            value,row_index,column_index = heappop(min_heap)
            counter += 1

            if counter == k:
                break
            
            if column_index + 1 <len(matrix[row_index]):
                heappush(min_heap,(matrix[row_index][column_index + 1],row_index,column_index + 1))
            
       return value