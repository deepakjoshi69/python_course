import random

num = random.randint(0,3)

random_choice = ["Stone", "Paper", "Scissor"]

user_choice = input("Enter your choice from 'Stone', 'Paper', 'Scissor' : ")

if user_choice == random_choice[num]:
    print("Tie!")

elif(user_choice == "Stone" and random_choice[num]=="Scissor" ):
    print(f"You won!, Computer Choice is {random_choice[num]}")

elif(user_choice == "Paper" and random_choice[num]=="Stone" ):
    print(f"You won!, Computer Choice is {random_choice[num]}")

elif(user_choice == "Scissor" and random_choice[num]=="Paper" ):
    print(f"You won!, Computer Choice is {random_choice[num]}")
    
else:
    print(f"You losse!, Computer Choice is {random_choice[num]}")