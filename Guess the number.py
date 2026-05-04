import random

target=random.randint(1,100)

while True:
    userChoice=input("Guess the target or Quit(Q): ").upper()
    if(userChoice == "Q"):
        break

    print(f"TARGET:{target}")

    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess!!")
        break
    elif(userChoice > target):
        print("Your number was too big. Take a smaller guess..!")
    else:
        print("Your number was too small. Take a bigger guess..!")    
print("GAME OVER")


            #OUTPUT
#Guess the target or Quit(Q): 34
#TARGET:41
#Your number was too small. Take a bigger guess..!
#Guess the target or Quit(Q): q
#GAME OVER
             
