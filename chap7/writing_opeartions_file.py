#  Writing to a File
# if your are using writing mode at any file it will remove all the prewrite text first 
file = open("demo.txt", "w")

data = file.write("i want to  learn agentic AI \ni wanna do something big in this field")

file.close()


file_name = open("demo.txt", "a")
inner_content = file_name.write("\ni want to become a rich")
file_name.close()

f = open("demo.txt", "r")
content = f.read()
print(content)
f.close()

# if we open a file  in append or write mode if it not exist  in the directory python will automatically create it 

r = open("file.txt", "w")
info = r.write("hi mi name is huzaif i am 18 years old")
r.close()
