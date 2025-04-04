#  functions

# function defination
def avg():
    a = int(input("enter a number 1 : "))
    b = int(input("enter a number 2 : "))
    c = int(input("enter a number 3 : "))
    average = (a + b + c) / 2
    print(f"the average of {a,b,c} is {average}")

    return "calculation complete"


z = avg()  # function call
print(z)




def greet():
    print("good day")

greet()