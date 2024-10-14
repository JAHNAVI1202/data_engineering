list_20_numbers=[i for i in range(1,21)]
print(list_20_numbers)
l=[]
for i in list_20_numbers:
    rem=i%3
    if(rem==0):
       l.append(i)
    else:
        print(rem,f"remainder for number {i}")
print(l)

  