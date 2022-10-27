import math
print("Hello world")
print("Hello world")
print(math.cos(3.65))
print("this will run")
a = 1
b = 3
c = "This is me"
d = 3.4
print(type(a))

str1 = "this is my first python string"
print(str1.lower())

items = ["harry", 2, 3]
items[1] = "Manish"
print(items)
tup1 = (1, 2, 3)
tup1[0] = 2
print(tup1)

dict1 = {}
print(type(dict1))
print(dict1)

dict1["virat"] = 100
dict1["sachin"] = 500
print(dict1.get("virat"))
print(dict1.items())
print(dict1.keys())

list1 = [1, 2, 3, 4, 4, 1]
s1 = set(list1)
print(s1)

a = 5
b = 10
c = "Harry"
print(str(a)+str(b)+c)
print("10 - 5 is ", 10-5)
print("10 * 5 is ", 10*5)
print("10 / 5 is ", 10/5)
print("10 + 5 is ", 10+5)


var = int(input())
print(var)
if(var > 4):
    print("Variable is greater")

elif(var == 2):
    print("Variable is two")

else:
    print("Variable is not greater")

for i in range(0, 101):
    print(i)
i = 0
while(i < 101):
    print(i)
    i = i+1


def average(num1, num2):
    avr = (num1 + num2) / 2
    return avr


print(average(3, 6))

index = 3

try:
    print(index)

except Exception as e:
    print(e)


f = open("1.txt", "w")
f.write("Subscribe to his channel for more")
f.close()
f = open("1.txt", "r")
content = f.read()
f.close()
print(content)
