# import random
# def snake_water_gun(player_choice):
#     choices = ["Snake", "Water", "Gun"]
#     computer_choice = random.choice(choices)
#     print(f"Computer's choice : {computer_choice}")
#     print(f"Player's choice : {player_choice}")
#     l1 = ["Draw", "Win", "Lose"]
#     if computer_choice == player_choice:
#         return l1[0]
#     elif ((player_choice == "Snake" and computer_choice == "Water") or (player_choice == "Water" and computer_choice == "Gun") or (player_choice == "Gun" and computer_choice == "Gun")):
#         return l1[1]
#     elif ((computer_choice == "Snake" and player_choice == "Water") or (computer_choice == "Water" and player_choice == "Gun") or (computer_choice == "Gun" and player_choice == "Gun")):
#         return l1[2]
#     else:
#         return -1

# dict1 = {"s": "Snake", "w": "Water", "g": "Gun"}
# while True:
#     a = input('''Enter :
#         1. 's' for Snake
#         2. 'w' for Water
#         3. 'g' for Gun
#         4. 'q' to Quit \n''')
#     a = a.lower()
#     if a == "q":
#         break
#     elif a not in dict1:
#         print("Invalid choice, please try again.")
#         continue
    
#     player_choice = dict1[a]
#     result = snake_water_gun(player_choice)
#     print(result)

import random

def check(comp, user):
    if comp == user:
        return 0
    if(comp == 0 and user == 1):
        return -1
    if(comp == 1 and user == 2):
        return -1
    if(comp == 2 and user == 0):
        return -1
    
    return 1



comp = random.randint(0, 2)
user = int(input("0 for Snake, 1 for Water and 2 for Gun :\n"))
print("You :", user)
print("Computer :", comp)

score = check(comp, user)
if(score == 0):
    print("It's a draw")
elif score == -1:
    print("You lose")
else:
    print("You won")
 