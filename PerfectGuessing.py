import random

number = random.randint(1,10)
userNumber = 0
guess = 0

while (userNumber!=number):
    userNumber = int (input("Enter the number: "))
    guess += 1
    if (userNumber==number):
        print("your guess is correct!!!!")
    else: 
        if (userNumber>number):
            print("your guess is not correct lower your number")
        elif (userNumber<number):
            print("your guess is not correct higher your number")

print("Number of guesses you took are:",guess)
with open("highScore.txt", "r") as f:
    hiscore = int(f.read())

if(guess<hiscore):
    print("You have just broken the high score!")
    with open("highScore.txt", "w") as f:
        f.write(str(guess))
