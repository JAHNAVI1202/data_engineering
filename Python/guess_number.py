import random
guess_number=random.randrange(1,20)
print(guess_number)  

chances =3
i=1
while(i<=chances):
    a=int(input("enter your Guess: ") )
    if guess_number == a:
       # i+=1
        print("you guessed it right")
        break
    else:
        i+=1
        print("Try again")

        

