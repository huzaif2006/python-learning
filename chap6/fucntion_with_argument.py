# function with arguments

def greetings(name):   #function parameter
    print(f"hi {name}")

greetings("Huzaif")  # function argument passing





# function with default parameter value 

def greet(name, ending="Thank you"):  # in this situation if user don't passing the argument in function call it will consider the default parameter value 
    print(f"Hello {name} ")
    print(ending)
greet("huzaif")
greet("john","thanks")