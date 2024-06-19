def findNumbers(nums):
    no = 0
    for i in range(0, len(nums)):
        if len(str(nums[i])) % 2 == 0:
            print("even")
            no +=1
        else:
            print("odd")
    return no
            
            
# nums = [12,34,56,724,24]
findNumbers([12,34,56,724,24])
        