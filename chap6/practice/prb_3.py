

def print_list(List:list, index:int):
    if(index == len(List)):
        return
    print(List[index]) 
    print_list(List, (index+1))


List:list = ["Huzaif", "kamran", "hashim", "ismail"]
index = 0

print(print_list(List, index))