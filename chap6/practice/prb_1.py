# prob 1 

def find_greatest(num1, num2, num3):
    if (num2 and num3) < num1:
        return f"num1 is the greatest one, which is {num1}"
    elif(num3 and num1) < num2:
        return f"num2 is the greatest one, which is {num2}"
    elif(num1 and num2) < num3:
        return f"num3 is the greatest one, which is {num3}"
    else:
        print("please enter number first")


num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
num3 = int(input("enter num3: "))

print(find_greatest(num1, num2, num3))