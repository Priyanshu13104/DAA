def prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print("the number is not prime")
                break
            else:
                print("the number is prime")
                break
    else:
        print("the number is not prime")
        
num = int(input("enter a number:"))
print(prime(num))