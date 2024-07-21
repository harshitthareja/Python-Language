# Strings are immutable
a = "!!! Harry !!!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry", "John"))
print(a.split(" "))
blogHeading = "introduction tO jS"
print(blogHeading.capitalize())
str1 = "Welcome to the Console!!!"
print(str1.center(50))
print(len(str1))
print(len(str1.center(50)))

print(a.count("Harry"))

str1 = "Welcome to the Console!!!"
print(str1.endswith("!!!"))

print(str1.endswith("to", 4, 10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("ishh"))
# print(str.index("ishh"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())
str1 = "hello world"
print(str1.islower())
str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())
str1 = "       "
print(str1.isspace())
str2 = "               "
print(str2.isspace())
str1 = "World Health Organization"
print(str1.istitle())
str1 = "Python is an Interpreted Language"
print(str1.startswith("Python"))
print(str1.swapcase())
print(str1.title())
