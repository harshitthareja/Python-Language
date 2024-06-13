marks = [3, 5, 6, "Harry", True]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])

# print(marks[-3]) # Negative index
# print(marks[len(marks)-3]) # Positive index
# print(marks[5-3]) # Positive index
# print(marks[2]) # Positive index

if "6" in marks:
    print("Yes")
else:
    print("No")

# Same thing applies for string as well
# if "arry" in "Harry":
#     print("Yes")

print(marks)
print(marks[1:-1])
print(marks[1:4])
print(marks[1:4:2])

lst = [i*i for i in range(10) if i%2 == 0]
print(lst)