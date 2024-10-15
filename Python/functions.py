def numbers_list(len,min_number,max_number):
    list_of_numbers=[]
    import random
    for i in range(1,len+1):
        list_of_numbers.append(random.randint(min_number,max_number))
    return list_of_numbers

list = numbers_list(20,1,100000)
print(list)
def append_num(new_num,list_num):
    list_num.append(new_num)
    return list_num
added_list= append_num(89000,list)
print(added_list)
def remove_num(remove_num,list_num):
    list_num.remove(remove_num)
    return list_num
removed_list= remove_num(89000,list)
print(removed_list)
def sort_list(list_to_sort):
     list_to_sort.sort(reverse=True)
     return list_to_sort
list.insert
desc_list = sort_list(list)
print(desc_list)
def inserted(list_m,num,index):
    
        list_m.insert(index,num)
        #list_m.append(num)
        
        return list_m

list_m= inserted(desc_list,80009,4)
print(list_m)