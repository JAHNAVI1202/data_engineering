list1=[1,2,3,4,5,7,80,70]
list1.sort(reverse=True)
print(list1[0],"is the largest")

print(list1[-1],"is the smallest")
print(list1,"is in desc order")
for i in list1:
    print(i, end=' ')
    sum=0
for i in list1:
    
    sum=sum+i
print("\n",sum, "is the sum of all numbers in list")
 
list2=["jahnavi", "How","are","you","every thing", "good"]
list_upper= [i.upper() for i in list2] #list comprehension

print(list_upper)

wish= "-".join(list_upper)

print(wish)#3
longest_str= max(list2,key=len)
shortest_str= min(list2,key=len)
print(longest_str)
print(shortest_str)