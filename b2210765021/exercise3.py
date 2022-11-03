import random
print("Guess a number between 1 and 25.")
guess=int(input("Please enter a number:"))
a=random.randint(1,25)
while guess!=a:
    if a<guess:
        print("Decrease your guess.")
        guess=int(input("Please enter a number:"))
    else:
        print("Increase your guess.")
        guess=int(input("Please enter a number:"))
if guess==a:
    print("yes,your guess is true")
        
