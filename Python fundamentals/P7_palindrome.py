s = input("Enter a string: ")
reverse_str = s[::-1]

if reverse_str == s:
    print("Yes, it is a palindrome.")
else:
    print("No, it is not a palindrome.")