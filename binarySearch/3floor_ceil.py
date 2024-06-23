import math
def floor_and_ceil(arr):
    floor=[]
    ceil=[]
    for i in range(len(arr)):
        floor.append(math.floor(arr[i]))
        ceil.append((math.ceil(arr[i])))

    return {'floor':floor,'ceil': ceil}

arr = [3.14, 2.33]
result = floor_and_ceil(arr)
print(result)