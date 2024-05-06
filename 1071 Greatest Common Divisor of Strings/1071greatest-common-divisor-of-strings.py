class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        def gcd(a,b):
            while b!= 0:
                a,b = b,a % b
            return a

        def canform(s,part):
            rep_count = len(s) // len(part)
            return part * rep_count == s

        gcd_length = gcd(len(str1),len(str2))

        candidate = str1[:gcd_length]

        if canform(str1,candidate ) and canform(str2,candidate):
            return candidate
        else:
            return ""

  
        