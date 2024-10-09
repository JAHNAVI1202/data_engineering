dict1={'jahnavi':98,'Aravind':100,'lucky':90,'dilli':89}

list = [ i for i in dict1.values()]
print(list)
list1 = [ i for i in dict1.keys()]
print(list1)

list.sort(reverse=True)
print(list)

print(list[0],"is the largest") 
print(list[-1],"is the smallest")

student_list = {'jahnavi':98,'Aravind':100,'lucky':90,'dilli':89}

print(student_list.get)
highest = max(student_list, key=student_list.get)
highest_score = student_list[highest]
lowest = min(student_list, key=student_list.get)
lowest_score =student_list[lowest]
print(f"{highest} :{highest_score}")
print(f"{lowest} :{lowest_score}")

student_list['siri'] = 44
print(student_list)

if 'Aravind' in student_list:
    del student_list['Aravind']
print(student_list)