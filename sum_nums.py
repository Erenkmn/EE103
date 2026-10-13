sum = 0
num = int(input("Enter a number to sum up to: "))
gauss_sum = num*(num+1)/2
for i in range(1, num + 1):
    sum += i
print("The sum of numbers from 1 to", num, "is", sum)
if sum == gauss_sum:
    print("My running sum code is working correctly")
else:
    print("My running sum code is not working correctly")

