def min_coins(coins, weight):
    dp = [float('inf')] * (weight + 1)
    dp[0] = 0
    
    for coin in coins:
        for x in range(coin, weight + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    return dp[weight] if dp[weight] != float('inf') else -1

coins = {10,5,25}
weight = 30
print(min_coins(coins, weight))