def max_num(arr):
    max = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > max:
            max = arr[i]
        
    print(max)

arr = list(map(int, input("Enter a list of numbers: ").split()))

max_num(arr)