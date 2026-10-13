result=1 
fac=int(input("Enter a number to calculate its factorial: "))
fac1=fac
while fac>0:
    result=result*fac
    fac=fac-1
print("The factorial of", fac1, "is", result)