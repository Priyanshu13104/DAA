class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]

        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        
        return result

solution = Solution()
nums1 = [4, 3, 2, 7, 8, 2, 3, 1]
nums2 = [1, 1]

print(solution.findDisappearedNumbers(nums1))  
print(solution.findDisappearedNumbers(nums2))  
