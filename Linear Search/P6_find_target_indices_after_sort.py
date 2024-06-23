def findTargetIndices(nums, target):
    arr=[]
    nums.sort()
    if target in nums:
        for i in range(len(nums)):
            if nums[i] == target:
                print(i)
                arr.append(i)
        return arr
    else:
        return []

nums1 = [1,2,5,2,3]
target1 = 2
print(findTargetIndices(nums1, target1))