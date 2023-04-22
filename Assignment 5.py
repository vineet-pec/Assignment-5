#Question 1
s = input(("Enter a sentence: "))
r = ''
i = len(s) - 1
while i >= 0 :
    r += s[i]
    i -= 1
print("The Reversed String is : ", r)

#Question 2
lower_num = int(input("Enter lower range limit : "))
upper_num = int(input("Enter upper range limit : "))
div_num = int(input("Enter the number that should be divided by : "))
for i in range(lower_num,upper_num+1):
   if( i%div_num==0 ):
      print(i)
else:
       print("Oops")

#Question 3
import math

a = int(input("Enter Value of side A: "))
b = int(input("Enter Value of side B: "))
c = int(input("Enter Value of side C: "))
if a+b > c and b+c > a and c+a > b:
    s = (a+b+c)/2
    print("The area of Triangle is: " ,math.sqrt(s*(s-a)*(s-b)*(s-c)))
else:
    print("The Triangle is Invalid.")

#Question 4
for i in range(1, 6):
    for j in range(1, i):
        print('* ', end='')
    print()
i = 5
while i >= 1:
    for j in range(i):
        print('* ', end='')
    print()
    i -= 1

#Question 5
list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
a = int(input("Enter the length of pattern required: "))
n = 0
for i in range(a + 1):
    for j in range(i):
        print(list[n%len(list)], end="")
        n += 1
    print()

#Question 6
r = int(input("Enter a the number till required: "))
print("The prime numbers are:")
for i in range(1, r + 1):
    div = 0
    for j in range(1, i + 1):
        if(i % j == 0):
            div += 1
    if(div == 2):
        print(i)

#Question 7
print ("The numbers which are multiple of 7 and divisible by 11 are: ")
for i in range(1, 501):
    if(i % 7 == 0 and i % 11 == 0):
        print(i)

#Question 8
list = []
bool = []
for i in range(10):
    list.append(int(input("Enter any number: ")))
    bool.append(False)
print('Positive numbers:')
for i in list:
    if (i > 0):
        print(i)
print('Negative numbers:')
for i in list:
    if (i < 0):
        print(i)
print('Odd numbers:')
for i in list:
    if (i % 2 == 1):
        print(i)
print('Even numbers:')
for i in list:
    if (i % 2 == 0):
        print(i)
print('Occurences')
for i in range(len(list)):
    c = 0
    if not bool[i]:
        for j in range(i, len(list)):
            if list[j] == list[i]:
                c += 1
                bool[j] = True
        print(list[i], ' occurs', c, ' times')

#Question 9
size = int(input('Enter size of list: '))
list = []
bool = []
for i in range(size):
    list.append(input("Enter the list items: "))
    bool.append(False)
for i in range(len(list)):
    c = 0
    if not bool[i]:
        for j in range(i, len(list)):
            if list[j] == list[i]:
                c += 1
                bool[j] = True
        print(list[i], ' occurs', c, ' times')



