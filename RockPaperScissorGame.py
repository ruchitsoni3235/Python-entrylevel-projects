"""
WORKFLOW OF PROJECT
1 - input from user(Rock, paper, Scissor)
2- Computer Choice ( Computer choose randomely not conditionally)
3 - Result Printed

cases :
A -Rock
Rock - Rock = tie
Rock - Paper = Paper
Rock - Scissor = Rock win

B-Paper
Paper - Paper = Tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C - Scissor
Scissor- Scissor = Tie
Scissor - Rock = Rock Win
Scissor - Paper = Scissor Win

"""

import random

item_list = ["Rock", "Paper", "Scissor"]
user_choice = input("Enter your move = Rock, Paper, Scissor=")
comp_choice = random.choice(item_list)

print(f"User Choice = {user_choice}, Computer Choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same: = Match Tie")
elif user_choice == "Rock":
    if comp_choice == "paper":
        print("paper covers rock = Computer wins")
    else:
        print("Rock Smashes scissor = You win")
elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor Cuts the paper, computer win")
    else:
        print("Paper covers rock, you win")
elif user_choice == "Scissor":
    if comp_choice == "paper":
        print("Scissor cuts the paper, you win")
    else:
        print("Rock Smashes Scissor, computer win")
