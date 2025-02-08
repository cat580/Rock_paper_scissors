import random

comp=random.choice(["rock","scissors", "paper"])
user= input("Do you want rock, paper, or scissors?")

print("computer choice:", comp)

if comp == user :
    print("Tie")
elif user == "rock" and comp == "scissors":
    print("user win")
elif user == "paper"  and comp == "rock":
    print("user win")
elif user == "scissors" and comp == "paper":
    print("user win")
else:
    print("you lose computer wins")

