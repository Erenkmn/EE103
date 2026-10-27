binary = ""
binary2= ""
num = float(input("Enter a number with decimal places: "))
numH = int(num //1)
numL=num %1

#for natural side (number High)
while True:
    if numH ==1 :
        binary += "1."
        break
    elif numH ==0:
        binary += "0."
        break
    temp = numH % 2
    binary += str(temp)
    numH //=2


#for decimal place (number Low)
#changed 22.th line because of part5
for  i in range (10):
    numL *= 2
    a = int(numL)
    binary2 += str(a)
    numL -= a
    if numL == 0.0:
        break


binary += binary2
print("Your number in binary is:" , binary)

