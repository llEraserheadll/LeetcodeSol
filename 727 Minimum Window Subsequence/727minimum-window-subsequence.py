class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        str1_size = len(s1)
        str2_size = len(s2)

        index_s1 = 0
        index_s2 = 0

        size = float('inf')
        min_sq = ''

        while index_s1 < str1_size:
            if s1[index_s1] == s2[index_s2]:
                index_s2 += 1
                if index_s2 == str2_size:
                    start = end = index_s1
                    index_s2 -= 1
                    while index_s2 >= 0:
                        if s1[start] == s2[index_s2]:
                            index_s2 -= 1
                        start -= 1
                    start += 1 #it takes an extra step back we are correcting it

                    if end - start < size:
                        size = end  - start
                        min_sq = s1[start : end + 1]
                    index_s1 = start
                    index_s2 = 0
            index_s1 += 1
        return min_sq


        