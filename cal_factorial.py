result = 1
fac = int(input("Enter a number to calculate its factorial: "))
for i in range(1, fac + 1):
    result *= i
print("The factorial of", fac, "is", result)

