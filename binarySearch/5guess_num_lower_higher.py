# Leetcode: https://leetcode.com/problems/guess-number-higher-or-lower/submissions/1295203157/
# IMP: EXECUTE THIS ONLY ON LEETCODE.
"""
Guess api call is given. I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        while start <= n:
            mid = start + (n - start) // 2
            result = guess(mid)
            if result == -1:
                n = mid - 1
            elif result == 1:
                start = mid + 1
            else:
                return mid