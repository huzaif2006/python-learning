#  problem 1
marks = {}

phy_marks = int(input("Enter phy marks : "))
chem_marks = int(input("Enter chem marks : "))
math_marks = int(input("Enter math marks : "))

marks.update({"phy" : phy_marks})
marks.update({"chem" : chem_marks})
marks.update({"math" : math_marks})

print(marks)


# problem 2

set1 = {
    ("float" ,9.0) , ("int",   9)
}
print(set1)