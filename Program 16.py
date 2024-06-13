# for i in range(1, 101, 1):
#     print(i, end = " ")
#     if(i == 50):
#         break
#     else:
#         print("Mississippi")
# print("Thank You")

# for i in range(12):
#     if(i == 10):
#         break
#     print("5 X", i+1, "=", 5 * (i + 1))
# print("Loop ko chhodkar nikal jao.")

# for i in range(12):
#     if(i == 10):
#         print("Skip the iteration.")
#         continue
#     print("5 X", i+1, "=", 5 * (i + 1))

i = 0
while True:
    print(i)
    i = i+1
    if(i%100 == 0):
        break