import random

while True:

    x = input("Enter R for Rock Enter P for Paper Enter S for Scissor Enter your choice: ")

    list = ["R","S","P"]
    c = random.choice(list)

    print("Computer chooses:", c)
    if x == c:
        print("You Both chooses same its a tie than")
    elif x == "R" and c == "S":
        print("You win")
    elif x == "S" and c == "P":
        print("You win")
    elif x == "P" and c == "R":
        print("You win")
    else :
        print("Computer WINS")
