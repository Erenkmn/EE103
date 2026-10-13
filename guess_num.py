from secret_number.py import secretNum 
counter = 0
guess = int(input("Guess the secret number between 1 and 10: "))
while guess != secretNum:
    counter +=1 
    if guess == secretNum:
        print("You answered correct!!!!")
        break
    else:
        print("Try again, you also have ",5-counter," chances left")
print("You used all your chances :'(")
