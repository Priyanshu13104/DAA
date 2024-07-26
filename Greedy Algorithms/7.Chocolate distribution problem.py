def chocolate_distribution(chocolates:list[int], M:int)->int:
    N = len(chocolates)

    if N < M:
        return -1

    chocolates.sort()
    min_diff = float('inf')
    i = 0
    j = M-1
    while i <= N-M:
        diff = chocolates[j] - chocolates[i]
        if diff < min_diff:
            min_diff = diff
        i += 1
        j += 1
    return min_diff

N = 8
M = 5
A = [3, 4, 1, 9, 56, 7, 9, 12]

print(chocolate_distribution(A, M))