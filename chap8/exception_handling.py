# num = input("enter a number: ")
# print(f"multiplication table of {num} is down below")


# try:
#     for i in range(1, 11):
#         print(f"{int(num)} x {i} = {int(num)*i}")
# except:
#     print("Invalid input")



# print("program end")








# try:
#     num = int(input("enter a num: "))
#     List = ["apple", "mango", "banana"]
#     print(List[num])
# except IndexError:
#     print("index out of range")
# except ValueError:
#     print("invalid input")










try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result is:", result)

except ZeroDivisionError:
    print("Oops! You can’t divide by zero.")

except ValueError:
    print("That’s not a number!")

else:
    print("Good job! You didn’t break anything.")

finally:
    print("The game is over.")

 