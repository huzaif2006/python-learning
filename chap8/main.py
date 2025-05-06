try:
    file = open("myfile.txt")
    content = file.read()
    print(content)

except FileNotFoundError:
    print("File nahi mili!")

finally:
    print("Program khatam ho gaya.")
