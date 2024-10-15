a = 'Hello Everyone'
print(len(a)) # length of the string

print(a[0])# first letter
print(a[-1]) # last letter
print(a[0:5:])# to print only Hello in a
print(a[6:14:])# Everyone in forward direction
print(a[-8::1])# Everyone in -ve indexing
print(a[0:5:1]) # Hello 
print(a[6:14:1]) # Everyone
print(a[0:5:2]) # Hlo
print(a[0:14:3]) # HlErn
print(a[-1::-1])
#or
print(a[::-1])
b=a.split()

print(b)
c= "hey!! how !! are !! you"
d= c.split("!!")
print(d)
print(a+c)
print(a*10)
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a)#immutable string
print("heyy:{}".format("hello"))










