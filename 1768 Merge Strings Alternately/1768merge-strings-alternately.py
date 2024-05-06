class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = []
        for char1,char2 in zip(word1,word2):
            merged.append(char1)
            merged.append(char2)

        if len(word1) > len(word2):
            remain = word1[len(word2):]
        else:
            remain = word2[len(word1):]

        merged.extend(remain)
        return ''.join(merged)