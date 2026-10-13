from secret_number import secretNum 
counter = 0
guess = int(input("Guess the secret number between 1 and 10: "))
while True:
    counter +=1 
    if guess == secretNum:
        print("You answered correct!!!!")
        break
    
    elif counter == 5:
          while True:
            print("Oh Noooooooooooo...")
        
    else:
        print("Try again, you also have ",5-counter," chances left")
        guess = int(input("Guess the secret number between 1 and 10: "))
