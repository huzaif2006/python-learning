#  Writing to a File

file = open("demo.txt", "w")

data = file.write("i want to  learn agentic AI \ni wanna do something big in this field")

file.close()


file_name = open("demo.txt", "a")
inner_content = file_name.write("\ni want to become a rich")
file_name.close()