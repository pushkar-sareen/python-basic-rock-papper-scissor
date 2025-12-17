import random
print("Type:- \n0 for Rock,\n1 for Papper, \n2 For scissor")

user_choice = int(input("what do you want to choose ? :" ))
computer_choice = random.randint(0, 2)

game = ["rock", "papper", "scissor"]
print(f"you choose {game[user_choice]}\ncomputer choose {game[computer_choice]}")


if user_choice >= 3 or user_choice < 0:
    print("please provide a valid input")
elif user_choice == 0 and computer_choice == 2:
    print("You Win!!!")
elif computer_choice == 0 and user_choice == 2:
    print("You Lose!!!")
elif user_choice > computer_choice:
    print("You Win!!!")
elif computer_choice > user_choice:
    print("You Lose!!!")
else:
    print("Draw!!")
