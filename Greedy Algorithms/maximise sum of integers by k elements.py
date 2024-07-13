def k_largest(nums: list[int], k:int)->int:
    nums.sort(reverse=True)
    sum = 0
    for i in range(k):
        sum += nums[i]
    return sum

print(k_largest(nums=[24, 3, -1, 2, 32, 12], k=3))