#      Lists

#  in python you can add multiple types of data in list

students: list = ["Huzaif", "Faraz", "muzammil", "sharukh"]

print(len(students))
students[0]= "Haider"  # you can excess and change the value of list in python with the help of index
print(students)


# slicing in list
# silicing in list is like a slicing in string 
marks: list = [45, 65.4, 88, 89.4, 76 ]

print(marks[0:2])
print(marks[1:4])
print(marks[1:])
print(marks[:4])
print(marks[-4:-1])




# Methods in list


List: list = [23, 45, 78, 56.6]

List.append(21)  # this method is used for adding one element at the end 
# in this scenario the list will be mutate means that the changes occurs in original list it will return none but it do changes in list
print(List) 
List.sort()          #this method is used sorting in list it sorts the list in ascending order
List.sort(reverse=True)    #this method is used sorting in list it sorts the list in descending order




# sort method also works on list of strings
Students = ["d", "a", "c", "b", "a"]

Students.sort()
Students.sort(reverse=True)
Students.reverse()  #this method is used for reversing original list 
Students.insert(0, "z")   # insert element at any index
Students.remove("a") # remove 1st occurence of element
Students.pop(2)  # remove element at any index
print(Students)



# Common functions of list 

Students.append("y") #you can write value in brackets that you want to inser in list
Students.sort()   # this methods can sort your list on ascending order 
Students.sort(reverse=True)  # this methods can sort your list on descending order 
Students.reverse()  #this method can reverse the whole list 
Students.insert(1, "f" ) #this method can insert element at any index 
Students.remove("a") #this method can remove the first occurence of an element
Students.pop(2)  #this method can remove element at any index 
 