def max_wealth(accounts):
    return max([sum(account)for account in accounts])

print(max_wealth([[1,2,3],[3,2,3]]))


