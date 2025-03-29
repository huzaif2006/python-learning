
# prob  ( sum of first n numbers)
i = 1
number = int(input("enetr a number: "))
sum = 0
while (i<= number):
    sum = sum +i
    i += 1

print(sum)


# prob  (factorial using for loop)
factorial = int(input('enter a number: '))
factorial_val = 1
range_func = range(1, factorial+1)

for i in range_func:
    factorial_val = factorial_val * i
    
print(factorial_val)



# prob   (factorial using while loop)
number = 5
factorial = 1
i = 1

while(i<=number):
    factorial = factorial * i
    i += 1


print(f"factoral of {number} = {factorial}")



