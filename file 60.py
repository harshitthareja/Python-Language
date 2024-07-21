import os
# os.rename("D:/Python Language/sample.txt", "D:/Python Language/sample2.txt")
files = os.listdir("D:/Python Language")
i = 1
for file in files:
    if file.endswith(".py"):
        print(file)
        os.rename(f"D:/Python Language/{file}", f"D:/Python Language/file {i}.py")
        i = i + 1