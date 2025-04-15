"""
characters                                  meaning
'r'                      open for reading (default)
'w'                      open for writing , truncating the file first means that it delete the the default text if it writes then write the new text or something
'x'                      create a new file and open it for writing
'a'                      open for writing, appending to the end of the file if its exist
'b'                      binary mode
't'                      text mode (default)
'+'                      open a disk file for updating (reading and writing)

"""


# Structure of open and closed file

"""
variable_name_that_return_file = open("filename.txt", "mode")
# --------------------------------------------------------------
content = variable_name_that_return_file.read()  #mode use on file
#                                                                   inner operations of file
print(variable_name_that_return_file)  #printing file ontent
# ---------------------------------------------------------------

variable_name_that_return_file.close()

"""

# file = open("demo.txt", "r")
# content = file.read()   # you can also pass the type 
# print(content)
# print(type(content))   #identifying the type of content
# file.close()


file = open("demo.txt", "r")

line1 = file.readline()     # you also read oneline throgh this function
print(line1 )

line2 = file.readline()
print(line2) 

file.close()



file = open("demo.txt", "r")

data = file.read()   # if you will read file all at once you cannot read it again line by line 
print(data)

line1 = file.readline()     # you can also read just one line
print(line1 )
line2 = file.readline()
print(line2) 
file.close()






 


