class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        int_start = newInterval[0]
        int_end = newInterval[1]
        output = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][0] < int_start:
            output.append(intervals[i])
            i += 1

        if not output or output[-1][1] < int_start : 
            output.append(newInterval)
        else:
            output[-1][1] = max(output[-1][1],int_end)
        
        while i < n :
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]

            if output[-1][1] < curr_start :
                output.append(intervals[i])
            else:
                output[-1][1] = max(output[-1][1],curr_end)
            i += 1
        return output

        