
# prob 1

def length_of_list(List:list):
    result = len(List)
    print(f"the length of list is {result}")


length_of_list(["huzaif", 2, "shariq", "akram",True])




# prob 2

def single_line(input:list):
    for item in input:
        print(item , end=" ") #built in parameter "end"    


single_line(["huzaif", "Kashan", "murtaza", "wajahat", 56])





# prob 3

def factorial_of_n(number:int):
    i = 1
    factorial = 1

    while(i <= number):
        factorial *= i
        i += 1
    print(factorial)


factorial_of_n(3)




# prob 4 

def currency_converter(USD:int):
    PKR = 280 
    conversion = USD*PKR
    print(f"{USD} USD = {conversion} PKR")

amount = int(input("How many USD you want to convert in PKR: "))
currency_converter(amount)



# prob 5

def identify_num(num):
    if (num%2 == 0):
        print(f"{num} is even ")
    else:
        print(f"{num} is odd")

identify_num(35)