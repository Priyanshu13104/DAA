def knapsack(values:list[int], weight:list[int], capacity:int)->float:
    N = len(values)
    items = [[weight[i], values[i]] for i in range(N)]
    # sort the items on value per unit of weight
    items.sort(reverse=True, key = lambda x:x[1]/x[0])
    total_value = 0.0
    current_w = 0
    for item in items:
        w, v = item[0], item[1]
        if current_w + w <= C:
            total_value += v
            current_w += w
        else:
            total_value = v*((C-current_w)/w)
            break
    return total_value


values = [60,100,120]
weight = [10,20,30]
C = 50

print(knapsack(values=values, weight=weight, capacity=C))
