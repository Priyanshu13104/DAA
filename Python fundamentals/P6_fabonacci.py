def fabonacci(num):
    nums = [0,1]
    if num == 0 or num == 1:
        print(nums)
        
    else:
        for i in range(1, num):
            sum = nums[-1 ] + nums[-2]
            nums.append(sum)
            print(sum)

fabonacci(10)