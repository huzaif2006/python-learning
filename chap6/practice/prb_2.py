# prob 2 

def sum_all(number:int):
    if number == 0:
        return 0
    
    return sum_all(number-1) + number


res = sum_all(10)
print(res)