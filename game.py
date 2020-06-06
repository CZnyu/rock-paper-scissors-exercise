print("Rock, Paper, Scissors, Shoot!")

def options (s):
    if s == "rock":
        return  "Rock"
    elif s == "paper":
        return "Paper"
    elif s == "scissors":
        return "Scissors"
    else:
        return "Hmmm...that's not an option. Try entering Rock, Paper, or Scissors"

print("--------------------")
selection = input("Enter Rock, Paper, or Scissors Here:")
item = options(selection)
print("You choose:", item)

