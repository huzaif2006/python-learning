
#  sets

# in python set are also a built-in data type the predefines elements of sets are immutable but we can add new element also 
# if we store any data in sets which are duplicate set will automatically ignored it and print it just one time 


set1 = {1, 2, 3, 4, 4, 4, 5, 5, 6, } 

print(type(set1))

pak_team = {"babar", "rizwan", "shaheen", "babar", "naseem",}  # sets have no order 
print(pak_team)
print(len(pak_team))  # in length function duplicate value will also ignore 



# way of declaring empty set

# set3 = set()  #empty set syntax
# print((set3))















# methods in sets

set4 = set()
set4.add(1)
set4.add(2)
set4.add(2)                   # it will ignore the duplicate value nd just print it one time
set4.add(5.7) 
set4.add("huzaif")
set4.add(("karachi", "lahore", "islamabad"))
set4.add(True)   
print(set4)           #in sets we can store all data type ehich are immutable we cannot store list and dicitionary beacuse they are mutable

set4.remove(("karachi", "lahore", "islamabad"))  # this methos will remove the elements of a sets
# set4.clear()  # this method will clear the set and make set empty
print(set4)
print(set4.pop())   # this method will randomly remove any element of the set


collection1 = {4,3,2,1}
collection2 = {7, 5,6,4,3}  # in the number of sets it will print the elements in ascending order

result = collection1.union(collection2)   # in union it will analyze the both set value and ignore all duplicate value and print all remainning values 
result1 = collection1.intersection(collection2)  # in intersection it will analyze both sets and print just those values that are same in both the sets
print(result)  #this methods will create new sets and make changes on it will not change any thing in existing set
print(result1)
print(collection1)
print(collection2)


collection3 = {"a", "c", "b", "s", "d"}
collection4 = {"x", "y", "z", "a"}
result2 = collection3.union(collection4)
print(result2)











