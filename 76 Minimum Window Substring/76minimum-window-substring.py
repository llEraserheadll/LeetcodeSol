class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t :
            return ''
        req_count = {}
        window = {}

        for i in range(len(t)):
            if t[i] not in req_count:
                req_count[t[i]] = 1
            else:
                req_count[t[i]] += 1
        
        current = 0
        required = len(req_count)
        left = 0
        result = [0,0]
        res_len = float('inf')

        for right in range(len(s)):
            char = s[right]
            if char in req_count:
                if char in window:
                    window[char] += 1
                else:
                    window[char] = 1
                
                if window[char] == req_count[char]:
                    current += 1
                
                while current == required:
                    if right - left + 1 < res_len:
                        result = [left,right]
                        res_len = right - left + 1
                    
                    left_char = s[left]
                    if left_char in req_count:
                        window[left_char] -= 1

                        if window[left_char]  < req_count[left_char]:
                            current -= 1
                    
                    left += 1
    

        return s[result[0]:result[1] + 1] if res_len != float('inf') else ''
        