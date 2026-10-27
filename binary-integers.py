integer = int(input("Enter an integer to convers binary form:"))
binaryForm = ""
while True:
    if integer ==1 :
        binaryForm += "1"
        break
    elif integer ==0:
        binaryForm += "0"
        break
    temp = integer % 2
    binaryForm += str(temp)
    integer //=2
    
print (f"Your number's binary form is:\n {binaryForm}\n")
