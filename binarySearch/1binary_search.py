#leetcode problem: https://leetcode.com/problems/binary-search/description/

"""
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""
class Solution(object):
    def search(self, nums, target):
        start = 0
        end = len(nums) - 1
        mid = int(start + end / 2)

        while start <= end:
            if target == nums[mid]:
                return mid
            else:
                if target > nums[mid]:
                    start = mid + 1
                    mid = int((start + end) / 2)
                elif target < nums[mid]:
                    end = mid - 1
                    mid = int((start + end) / 2)
                else:
                    return mid
        return -1


nums = [-1, 0, 3, 5, 9, 12]

bs = Solution()

result = bs.search(nums, target=0)
print(result)
