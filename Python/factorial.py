
def fact(num):
    
    prod=1
    
    for i in range(1,num+1):
        prod=prod*i
    return prod
number=int(input("enter the number to find  the factorial : "))

fac = fact(number)
print(f"{fac} is a factorial of number {number}")