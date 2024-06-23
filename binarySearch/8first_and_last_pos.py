class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end=0,0
        if target in nums:
            for i in range(len(nums)):
                if start != 0:
                    start=i
                elif target == nums[i]:
                    end=i
            return [start, end]

        else:
            return [-1, -1]


nums = [1]
target = 1
sol = Solution()
print(sol.searchRange(nums, target))