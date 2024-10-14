score=int(input("Please enter your score : "))
if score >=0 and score <=100:
    if(score>90):
        print("your grade is A")
    elif(score>=80 and score <=89):
        print("your grade is B")
    elif(score>=70 and score <=79):
        print("your grade is C")
    elif(score<70):
        print("your grade is D")
    
else:
    print("enter a valid score")
