import random
user_choice = int(input("enter your choice: type 0 for rock ,1 for paper,2 for scissors."))
if user_choice >= 3 or user_choice < 0 :
   print (" you entered invalid num ,you lose")
else:
    computer_choice = random.randint(0,2)
    print(" computer chose:")
    print( computer_choice)
    if computer_choice == user_choice :
       print(" it's draw ")
    elif computer_choice == 2 and user_choice ==0:
       print("you win ")
    elif computer_choice == 0 and user_choice ==2:
       print ("you lose")
    elif computer_choice > user_choice :
       print(" you lose")
    elif user_choice > computer_choice :
       print("you win")
