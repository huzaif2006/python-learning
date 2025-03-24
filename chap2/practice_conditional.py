
#  problem 1

marks = int(input("what's your marks : " ))

if(marks >= 90):
    grade = "A"
elif(marks < 90 and marks >= 80):
    grade = "B"
elif(marks >= 70):
    grade = "C"
elif(marks >= 60):
    grade = "D"
elif(marks >= 50): 
    grade = "E"
else:
    grade = "Fail"

print("your grade is", grade)





# problem 2

num = int(input("enter the number "))

if(num%2 == 0):
    number = "even"
else:
    number = "odd"

print("your number is ",number)






# problem 3

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

print(num1 , num2 , num3)

if(num1 > num2 and num1 > num3 ):
    print(num1 , "is gretest")
elif(num2 > num1 and num2 > num3):
    print(num2 , "is gretest")
elif(num3 > num1 and num3 > num2):
    print(num3 , " is the gretest")
else:
    print("please enter the number")





# problem 4

value = int(input("enter a number : "))

if(value % 7 == 0):
    print(value, "yes this number is the multiple of 7")
else:
    print(value , "No this number is not the multiple of 7")