# Another metohod of opening file in this method you do not need to used close method

with open("index.txt", "w+") as file:
    file.write("hi i'm a future Agentic AI developer")
    # file.seek(0)
    print(file.read())



with open("index.txt", "a+") as file:
    file.write("hi i'm Huzaif")
    file.seek(0)
    print(file.read())
    