"""part1: Recap


std_num = int(input("Enter your student number: "))
print(f"Hello, my student number is {std_num}!") 


name = "eren güler"
name1 = name.upper()
print(name1)
name2 = name[::-1]
print(name2)

this_year = "2026"
first_two_digits = this_year[0:2]
last_two_digits = this_year[2:4]
my_sum = int(first_two_digits) + int(last_two_digits)
print(f"{my_sum:.2f}")
if my_sum == 46:
    print("Correct")
else:
    print("Wrong")  """

""" part2
multipier = 1
for i in range (7,18+1):
    multipier *= i
print(f"answer is :{multipier}") """

""" part3:
s = "sdljhwefouwfhykckjlvss"
print(f"s({s}) has {len(s)} characters \n")
container = ""
for i in s:
    if i not in container:
        container += i

print(f"Unique characters in s: {container}")
print(f"s has {len(container)} unique characters")
 """

""" part4:
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if b==a-2 and c==a*2 and a+b+c == 10:
                print(f"allysa:{a}  ")
                break """
""" part5:
for a in range(1, 1000):
    for b in range(1, 1000):
        for c in range(1, 1000):
            if b==a-20 and c==a*2 and a+b+c == 1000:
                print(f"allysa:{a}  ") 

                        
   or 


a =0 
b = 20
c = 0
while True:
    if  a+b+c == 1000:
        print(f"allysa:{a}  ")
        break
    a+= 1
    b+= 1
    c+= 2                
"""

x = 0
for i in range(10):
    x += 0.1
print(x)
