class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        count = [0] * (n+1)

        for c in citations:
            count[min(n,c)] += 1

        paper = count[n]
        h = n

        while h > paper:
            h -= 1
            paper+=count[h]
        
        return h
