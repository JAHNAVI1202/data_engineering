def palindrome(string):
    reverse=string[::-1]
    if(string==reverse):
        return string
    
str=input("enter a string:  ")
palin =palindrome(str)
print(palin,"is a palindrome number")
