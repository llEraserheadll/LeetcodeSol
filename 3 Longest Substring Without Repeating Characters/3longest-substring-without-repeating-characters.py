class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        window_length,window_start,longest = 0,0,0
        last_seen_at = {}

        for index,val in enumerate(s):
            if val not in last_seen_at:
                last_seen_at[val] = index
            else:
                if last_seen_at[val] >= window_start:
                    window_length = index - window_start
                    if window_length > longest:
                        longest = window_length
                    window_start = last_seen_at[val] + 1
                last_seen_at[val] = index
        
        index += 1
        if longest < index - window_start:
            longest = index - window_start
        
        return longest
        