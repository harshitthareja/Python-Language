# def average(a, b, c=1):
#     print("The average is", (a+b+c)/2)
# average(b=9)

# def name(fname, mname = "Jhon", lname = "Whatson"):
#     print("Hello,", fname, mname, lname)
# name("Amy", "Aggarwal", "Jain")

# average(5, 6)

def average(*numbers):
    # print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum+i
    # print("Average is :", sum/len(numbers))
    return sum / len(numbers)
c = average(5, 6)
print(c)

# def name(**name):
#     print(type(name))
#     print("Hello,", name["fname"], name["mname"], name["lname"])
# name(mname = "Buchanan", lname = "Barnes", fname = "James")