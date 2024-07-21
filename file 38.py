# # READING A FILE

# f = open("myfile.txt", "r")
# # print(f)
# text = f.read()
# print(text)
# f.close()

# # WRITING TO A FILE

# f = open("myfile.txt", "a")
# f.write("Hello World")
# f.close()

with open("myfile.txt", "a") as f:
    f.write("Hey I am inside with")