n = int(input("Enter a number : "))  # it takes input

for i in range(2, n):   # loop will run and start from 2 
    if(n%i) == 0:  # if remainder of n divided by current iteration i s equak to 0 it will prints num is not prime  
        print("num is not prime")
        break    # if the condition will true it will break the code and exit from the loop
else:
    print("num is prime")  # if the condition of for block is not true it will print this code
        
   
        