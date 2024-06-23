def binary_search_2D(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if target == arr[i][j]:
                return [i, j]

arr = [[3, 12, 9], [5, 2, 89], [90, 45, 22]]
target = 45
print(binary_search_2D(arr, target))