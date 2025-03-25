


# prob 1 

fav_movies = []

fav_movies.append(input("tell me the first movie you like : "))
fav_movies.append(input("tell me the second movie you like : "))
fav_movies.append(input("tell me the third movie you like : "))

print(fav_movies)







# prob 2 

# palindrome : ese lafz jo shuru s prhay jaye to jabhi wohi pronunciation ho or jab akhir s prhay jaye to bhi same pronounciation ho 


List1 = [1, 2, 1]
copy_list1 = List1.copy()
copy_list1.reverse()

if (copy_list1 == List1):
    print("list is palindrome")
else:
    print("list isn't palindrome")






# prob 3

grades = ("C", "D", "A", "A", "B", "B", "A")


result = grades.count("A")
print(f"the number of A grade students are {result}")


Sorting = ["C", "D", "A", "A", "B", "B", "A"]
Sorting.sort()
print(Sorting)




# prob 4

num1 = int(input("enter 1st num : "))
num2 = int(input("enter 2st num : "))

sum = num1 + num2
differnce = num1-num2
quotient = num1 / num2
product = num1 * num2


print(sum)
print(differnce)
print(quotient)
print(product)
