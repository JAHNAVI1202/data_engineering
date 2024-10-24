#1
def separate_and_sums(lista):
    even_list = [num for num in lista if num % 2 == 0]
    odd_list = [num for num in lista if num % 2 != 0]

    even_sum = sum(even_list)
    odd_sum = sum(odd_list)

    if even_sum >= odd_sum:
        return even_list, even_sum
    else:
        return odd_list, odd_sum

lista = [1,2,3,4,5,6,7,8]
print(f"The Result of the Separate and Sums for a given list is {separate_and_sums(lista)}")
#2
def letter_histogram(word):
    out = {}
    for letter in word:
        if letter in out:
            out[letter]+=1
        else:
            out[letter] = 1
    return out

word = "banana"
print(f"The Result of letter histogram  for a given word is {letter_histogram(word)}")

#3
count = 0 
num=20
for i in range(1, num+1):
    count = 0 
    if num % i == 0:
        count = count+1
    else:
        pass
if count == 2:
    print("It is a Prime")
else:
    print("It is not a prime")


#
l = []
l.append(2)
for i in range(3, num+1,2):
    count=0
    for j in range(1,i+1):
        if i % j == 0:
            count = count+1
    if count == 2:
        l.append(i)
print(f"Prime Number until {num} are {l}")
#
count = 0 
num = 18
if num <= 1:
    print(f"{num} is not a prime number")
if num == 2 or num == 3:
    print(f"{num} is a prime number")
for i in range(4, num+1,):
    if num % i == 0:
        count = count+1
    if count == 2:
        print("It is a Prime")
    else:
        print("It is not a prime")
#
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True

num = 1801013
if is_prime(num):
    print(f"{num} is a prime")
else:
    print(f"{num} is not a prime")
#
students = {
    "Alice": {"Math": 80, "English": 75, "Science": 90},
    "Bob": {"Math": 70, "English": 85, "Science": 75},
    "Charlie": {"Math": 95, "English": 60, "Science": 85}
}

def cal_avg(students):
    avg = {}
    for student, subjects in students.items():
        total = 0
        num = len(subjects)
        for mark in subjects.values():
            total+=mark
        avg[student] = round(total/ num, 2)
    print(avg)
    
    top_student = max(avg, key=avg.get)
    return top_student

print(f"Our top student with most highest average is {cal_avg(students)}")
