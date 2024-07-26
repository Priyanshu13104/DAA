def candy_price(candies :list[int], k:int)->[int, int]:
    candies.sort()
    # compute min price
    N = len(candies)
    min_p = 0
    buy = 0
    free = N - 1
    while buy <= free:
        min_p += candies[buy]
        buy += 1
        free -= k

    # compute max price
    max_p = 0
    buy2 = N - 1
    free2 = 0
    while buy2 >= free2:
        max_p += candies[buy2]
        free2 += 1
        buy2 -= 1

    return min_p, max_p


k = 2
candies = [3, 2, 1, 4]
print(candy_price(candies, k))