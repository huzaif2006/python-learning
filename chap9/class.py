#  object is  also called instance 

# simple class

# class Student:
#     name = "Huzaif"
   

# # student 1
# s1 = Student()
# print(s1.name)
# # student 2
# s2 = Student()
# print(s2.name)








# class with constructor function

class Teacher:
    def __init__(self, full_name):   #self alway be a first parameter it is used for creating object or instance
        self.name = full_name
        

teacher1 = Teacher("huzaif")
print(teacher1.name)

teacher2 = Teacher("hamza")
print(teacher2.name)

