class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        start = 1
        end = x

        while start <= end:
            mid = start + (end - start) // 2
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                end = mid - 1
            else:
                start = mid+ 1
        return end

sol = Solution()
print(sol.mySqrt(16))