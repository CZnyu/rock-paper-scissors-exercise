print("Rock, Paper, Scissors, Shoot!")

import random

arr = ["Rock","Paper","Scissors"]

def options (s):
    if s == "Rock":
        return  arr[0]
    if s == "rock":
        return  arr[0]
    elif s == "Paper":
        return arr[1]
    elif s == "paper":
        return arr[1]
    elif s == "Scissors":
        return arr[2]
    elif s == "scissors":
        return arr[2]
    else:
        return ("Hmmm...that's not an option. Try entering Rock, Paper, or Scissors", quit)



print("--------------------")
user_choice = input("Enter Rock, Paper, or Scissors Here: ")
item = options(user_choice)
print("YOU CHOSE:", item)

computer_choice = random.choice(arr)
print(f"COMPUTER CHOSE: '{computer_choice}'")

outcomes = {
    arr[0]:{
        arr[0]: None,
        arr[1]: arr[1],
        arr[2]: arr[0],
    },
    arr[1]:{
        arr[0]: arr[1],
        arr[1]: None,
        arr[2]: arr[2],
    },   
    arr[2]:{
        arr[0]: arr[0],
        arr[1]: arr[2],
        arr[2]: None,
    },   
 }



winning_choice = outcomes[user_choice][computer_choice]

if winning_choice:
    if winning_choice == user_choice:
        print("YOU WON")
    elif winning_choice == computer_choice:
        print("YOU LOST")
else:
        print("TIE")
print("Thanks for playing. Please play again!")