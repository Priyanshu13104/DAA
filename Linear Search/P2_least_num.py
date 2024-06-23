def least_num(arr):
    least = arr[0]
    for i in range(1,len(arr)):
        if arr[i] < least:
            least = arr[i]
        
    print(least)

arr = list(map(int, input("Enter a list of numbers: ").split()))

least_num(arr)