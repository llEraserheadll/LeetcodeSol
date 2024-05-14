class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        reverse = words[::-1]
        result = ' '.join(reverse)

        return result