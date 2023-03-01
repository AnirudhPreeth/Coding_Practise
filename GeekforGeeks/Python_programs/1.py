#1. Python program to add two numbers.

number1 = int(input("First number:  "))
number2 = int(input("Second number: "))
sum = number1 + number2
print(f"The sum of the two numbers is: {sum}.")

num1 = 20
num2 = 20
sum = num1 + num2
print(sum)
#The above is my solution to the problem. 
#Solution.
num1 = 15
num2 = 12
sum = num1 + num2
print("Sum of {0} and {1} is {2}" .format(num1, num2, sum))

number1 = input("First number: ")
number2 = input("\nSecond number: ")
sum = float(number1) + float(number2)
print("The sum of {0} and {1} is {2}" .format(number1, number2, sum))

if __name__ == "__main__" :
   
  num1 = 15
  num2 = 12
  sum_twoNum = lambda num1, num2 : num1 + num2
  print("Sum of {0} and {1} is {2};" .format(num1, num2, sum_twoNum(num1, num2)))

def add(a,b):
  return a+b
num1 = 10
num2 = 5
sum_of_twonumbers = add(num1,num2)
print("Sum of {0} and {1} is {2};" .format(num1, num2, sum_of_twonumbers)) 

num1 = 15
num2 = 12
import operator
su = operator.add(num1,num2)
print("Sum of {0} and {1} is {2}" .format(num1, num2, su))

#2. Maximum of two numbers in Python.

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
if num1 > num2:
    print(f"The greater number is {num1}.")
else:
    print(f"The greater number is {num2}.")
#The above is my solution to the problem. 
#Solution.
def maximum(a, b):
    if a >= b:
        return a
    else:
        return b
a = 2
b = 4
print(maximum(a, b))

a = 2
b = 4
maximum = max(a, b)
print(maximum)

a = 2
b = 4
print(a if a >= b else b)
 
a=2;b=4
maximum = lambda a,b:a if a > b else b
print(f'{maximum(a,b)} is a maximum number')

a=2;b=4
x=[a if a>b else b]
print("maximum number is:",x)

a = 2
b = 4
x=[a,b]
x.sort()
print(x[-1])

#3. Python Program for factorial of a number.


