# prob 1 

# a = 1

# while a<=100:
#     print(a)
#     a += 1



# prob 2 

# b = 100

# while b>= 1:
#     print(b)
#     b = b - 1

# prob 3

# i = 1
# j = int(input("enter a number "))

# while i <= 10:
#     print(f"the table of {j} is {j *i}")
    
#     i += 1


# prob 4

# nums = [1, 4, 6, 7, 10, 16, 19, 25, 33, 40]

# index = 0

# while index < len(nums):
#     print(nums[index])
#     index = index + 1

# prob 5

# heroes = ["superman", "Iron man", "Flash", "Spider man"]

# idx = 0

# while idx < len(heroes):    # when we go to each of things in programming we called it traverse    (traverse means travel)
#     print(heroes[idx])
#     idx += 1



# prob 6

numbers = [1, 4, 6, 7, 10, 16, 19, 25, 33, 40]  # predefined list
i = 0  #initial loop vriable
input = 16 # input from the user

while i < len(numbers):   # it will run until the condition will false
    if(input == numbers[i]):   #on this line it check input from user is equal to the element of an index 
        print( f"{input} is exist on index {i}")  # if condition will true it prints this 
        break
    else:
        print("finding....")           #if condition will not true its print this line of code 
    i += 1  # this line add 1 on every iteration

