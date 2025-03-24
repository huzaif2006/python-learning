#                                                strings


# in python there are three ways to define string 

first_name = 'Huzaif'

City = "Karachi"

# This string method is used for dividing in multiple lines

my_self = """I am Huzaif
I live in karachi
and I am 18 years old"""


print(first_name)
print( City)
print( my_self)



# method to know about the length of string

country = "Pakistan"

# this function also count whitespces in string

res = len(country)
print(res)







# slicing in string

Movie = "Fast and furious"
# slicing alway start from definning index and ends on before ending on closing index
Movie[1:8]
 
Movie[:8] # if we write just this will consider from starting index position to current index
Movie[1:] # if we write just this will consider from current index position to ending index position
Movie[6:len(Movie)] # if we write just this will consider from current index position to whole length of string

# we cam also do negative indexing in python the negative indexing start feom -1 from ending of string
print(Movie[-16:-12])
print(Movie[-5:-1])  




#  functions that applies on string
Str = "i am codera"
print(Str.endswith('dera')) #this function identifies on which words string ends if the function argument will correct it will return True otherwise False
print(Str.capitalize()) #this function will capitalize the first letter of string
# this function will replace the letter or words from string in this function we will pass first old letter or word that we want to replace and then new word that we want show on the place of new word
print(Str.replace("codera", "programmer")) 
print(Str.replace("a", "e"))
# return first index of the letter or word where it placed
print(Str.find("e")) 
print(Str.find("H")) #return -1 if the word or letter not exist on string
print(Str.count("a"))  #return the repeatition of word or letter in string 