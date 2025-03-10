class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        most_char_freq = 0
        substring_length = 0
        freq = {}
        size = len(s)

        for end in range(size):
            if s[end] not in freq:
                freq[s[end]] = 1
            else:
                freq[s[end]] += 1
            
            most_char_freq = max(most_char_freq , freq[s[end]])

            if end - start + 1 - most_char_freq > k :
                freq[s[start]] -= 1
                start += 1
            
            substring_length = max(substring_length , end - start + 1)
        
        return substring_length
        