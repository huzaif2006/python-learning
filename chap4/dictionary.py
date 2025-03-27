
student1 = {
    "name" : "Huzaif",
    "roll no" : 89470,
    "marks" : 85.6,
    "subjects": ["islamiyat", "pst", "math", "physic"],
    "topics" : ("dictionary", "sets"),
    "is_adult" : True
}


student1["name"] = "khan"
student1["surname"] = "bhai"     #we can also add new key value pairs in dictionary like this

print(student1)


null = {}  # we can also create an empty dicitionary and then add key value pairs later

null["name"] = "Huzaif"
print(null)




student = {                        # WE CAN ALSO CREATE NESTED DICITIONARY LIKE THIS
    "name" : "Haroon",
    "subjects" : {
        "english" : 89,
        "maths" : 78.4,
        "Urdu" : 88
    }
}

res = student["subjects"]["maths"]
print(res)






# Methods of Dicitionary


teacher = {
    "name" : "Zain",
    "subjects" : ["english", "maths", "urdu"],
    "classes" : (3, 4, 5)
}

print(len(teacher))
print(teacher.keys())  #this method is used for print just keys of an dicitionary
print(list(teacher.keys()))  #you can also do type casting in getting keys from dicitionary
print(teacher.values())    # with the help of this method you can print just value of dicitionary
print(teacher.items())    # return all key value pairs in the form of tuple 
print(teacher.get("name"))  # return value according to key
teacher.update({"city" : "Karachi"  })  #you can add some more key value pairs and also update the value of key through this method
print(teacher)
