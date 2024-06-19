def find_char(char, string):
    for i in range(0, len(string)):
        if string[i] == char:
            print("the character is in the string")
            break
        else:
            print("the character is not in the string")
            
find_char("r","Priyanshu")