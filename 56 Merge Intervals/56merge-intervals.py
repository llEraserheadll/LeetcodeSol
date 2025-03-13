class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return None
        
        intervals.sort(key = lambda x : x[0])
        output = []
        output.append([intervals[0][0],intervals[0][1]])

        for i in range(1,len(intervals)):
            last_item = output[len(output) - 1]
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]
            prev_end = last_item[1]

            if curr_start <= prev_end:
                output[-1][1]  = max(curr_end,prev_end)
            else:
                output.append([curr_start,curr_end])
        return output
        