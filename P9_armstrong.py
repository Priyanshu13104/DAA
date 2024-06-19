def is_armstrong(n):
    sum = 0
    temp = n
    while temp:
        sum += (temp % 10) ** 3
        temp = temp // 10
    return sum == n

n = int(input("Enter a number: "))
if is_armstrong(n):
    print(n, "is an armstrong number.")
else:
    print(n, "is not an armstrong number.")