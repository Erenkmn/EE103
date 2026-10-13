givenNum = int(input("Enter a number for cube root: "))
if givenNum < 0:
    print("Cannot compute cube root of a negative number.")
else:
    guessNum = 0
    while guessNum ** 3 < givenNum:
        guessNum += 1
    if guessNum ** 3 == givenNum:
        print(f"The cube root of {givenNum} is {guessNum}.")
    else:
        print(f"{givenNum} is not a perfect cube. The closest integer cube root is {guessNum - 1}.")
        