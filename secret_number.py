SecretNumber = 35
#for Izmir :))
YourNumber = int(input("Guess the secret number: "))
while True:
    if YourNumber == SecretNumber:
        print("\n !! You guessed it right !!")
        break
    else:
        print("\n \n Sorry, It is not true :( \n Hint: İt must have 2 digits .")
    YourNumber = int(input("\n Guess the secret number: "))
    