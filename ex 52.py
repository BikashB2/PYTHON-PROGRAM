def palindrome(s):
    return  s == s[::-1]
a=str(input("Enter string:"))
if(palindrome(a)==True):
    print("String is a palindrome!")
else:
    print("String isn't a palindrome!")