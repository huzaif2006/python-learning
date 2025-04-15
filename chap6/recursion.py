# #           Recursion

# '''
# factorial(0) = 1
# factorial(1) = 1
# factorial(2) = 2 x 1
# factorial(3) = 3 x 2 x 1
# factorial(4) = 4 x 3 x 2 x 1
# factorial(5) = 5 x 4 x 3 x 2 x 1

# factorial(n) = n x (n-1) x .... x 2 x 1

# '''

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)
    


"""
4 x 3 = 12

"""


print(factorial(4))




def show(n):
    if n == 0:
        return
    print(n)
    show(n-1)


show(9)



def num(number):
    if(number == 0):
        return
    else:
        print(number)
        num(number-1)


num(4)