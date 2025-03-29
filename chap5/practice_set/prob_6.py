# the method of findng factorial of any number is multiply with all the numbers from 1 to the current number you are working on 

#  5! = 1 x 2 x 3 x 4 x 5 
#  6! = 1 x 2 x 3 x 4 x 5 x 6   

factorial = 6
current_factorial_val = 1

for i in range(1, factorial+1):
    current_factorial_val = current_factorial_val * i
    


print(f" the factorial of {factorial} is {current_factorial_val}")
