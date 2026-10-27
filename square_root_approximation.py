import math
number = int(input("Enter a number to calculate squareroot aproximately:"))
answer = math.sqrt(number)
top= number
end= 0
avg = (top+end)/2
epsilon = abs(answer-avg)
while epsilon > 0.00001:
    if avg > answer:
        top = avg
    else:
        end = avg
    avg = (top+end)/2
    epsilon = abs(answer-avg)
print("squareroot of ",number ,"is approximately " , avg)
