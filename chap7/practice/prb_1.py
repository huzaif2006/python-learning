
def Double_num(user_input):
    while(user_input < 100):
        print(user_input)
        user_input += user_input
    return user_input

user_input = int(input('Enter the number you want to double it: '))
result = Double_num(user_input)
print(result)

# user_input = int(input("enter a number: "))

# while user_input <= 100 :
#     user_input *=2f
#     print(user_input)








# def double_num(num):
#     while num <= 100:
#         num *= 2
#         print(num)


# double_num(2)