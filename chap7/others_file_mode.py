#  r+ mode is used for writing and readig data in file
# in this file pointer start from  the starting of the file and overwrite on the existing text
# this mode will not truncate(means: it will not remove the existing text first) the file first
file = open("sample.txt", "r+")
content = file.write("hello")
print(file.read())
file.close()





# W+ mode is also used for reading and writing data in file  but it will truncate all data first then write anything


file_name = open("sample.txt", "w+")
file_name.write("hi my name is huzaif")
file_name.seek(0)   #  seek function is used for moving cursor
print(file_name.read())

file_name.close()