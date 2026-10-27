givenNum = int(input("Enter a number for square root: "))
if givenNum < 0:
    print("Cannot compute square root of a negative number.")
else:
    guessNum = 0
    while guessNum * guessNum < givenNum:
        guessNum += 1
    if guessNum * guessNum == givenNum:
        print(f"The square root of {givenNum} is {guessNum}.")
    else:
        print(f"{givenNum} is not a perfect square. The closest integer square root is {guessNum - 1}.")
        