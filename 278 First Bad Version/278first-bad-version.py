# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        first = 1
        last = n

        while first <= last:
            mid = first + (last-first) // 2

            if isBadVersion(mid):
                last = mid - 1
            else:
                first = mid + 1
        return first