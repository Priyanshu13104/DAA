import math


def island_survival(N:int, S:int, M:int)->int:
    sundays = S // 7
    buy_days = S - sundays
    total_food = S * M
    total_days = math.ceil(total_food / N)
    if total_days <= buy_days:
        return total_days
    else:
        return -1


S = 10 #survival days
N = 16 # total food
M = 2 # food per day

print(island_survival(N, S, M))