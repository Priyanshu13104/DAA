#leetcode: https://leetcode.com/problems/first-bad-version/
#FIRST BAD VERSION

"""
This program cannot be executed locally as it involves api calls and functions provided
by leetocode. This is the solution to solve the problem
"""
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n

        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left