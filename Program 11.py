# a = int(input("Enter your age"))
# print("Your age is :", a)
# if(a > 18):
#     print("You can drive")
# else:
#     print("You cannot drive")
# applePrice = 10
# budget = 200
# if(budget - applePrice > 50):
#     print("Alexa, add 1 kg Apples to the cart.")
# elif(budget - applePrice > 70):
#     print("It's okay you can buy")
# else:
#     print("Alexa, do not add Apples to the cart.")
# num = int(input("Enter the value of num : "))
# if(num < 0):
#     print("Number is negative.")
# elif(num == 0):
#     print("Number is Zero.")
# else:
#     print("Number is positive.")
# print("I am happy now.")
num = 18
if(num < 0):
    print("Number is negative.")
elif(num > 0):
    if(num <= 10):
        print("Number is between 1-10.")
    elif(num > 10 and num <= 20):
        print("Number is between 11-20.")
    else:
        print("Number is greater than 20.")
else:
    print("Number is Zero.")