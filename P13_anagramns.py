def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if is_anagram(s1, s2):
    print("Yes, they are anagrams.")
else:
    print("No, they are not anagrams.")