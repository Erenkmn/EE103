start = int(input("This is a multiplier, only work in integers. \n Enter a start point:"))
end = int(input("Enter a end point:"))



result_for = 1
for i in range(start,end+1):
    result_for *= i
print(f"Your (for) result is ==> {result_for}")

result_while = 1
while start != end+1:
    result_while *= start
    start +=1
print(f"Your (while) result is ==> {result_while}")

if result_while == result_for:
    print("\nResults are same\n")
else :
    print("\nResults are different\n")
