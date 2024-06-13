# user_input = input("Enter e/E to encode and d/D to decode: ")
# try:
#     if user_input == "e" or user_input == "E":
#         str1 = input("Enter the word you wish to encode: ")
#         if len(str1) < 3:
#             str1 = str1[::-1]
#         else:
#             str1 = str1[1:] + str1[0]
#             str1 = "min" + str1 + "kid"
#         print("The encoded string is:", str1)
#     elif user_input == "d" or user_input == "D":
#         str1 = input("Enter the word you wish to decode: ")
#         if len(str1) < 3:
#             str1 = str1[::-1]
#         else:
#             str1 = str1[3:-3]  # Remove the 'min' prefix and 'kid' suffix
#             str1 = str1[-1] + str1[:-1]  # Move the last character to the front
#         print("The decoded string is:", str1)
#     else:
#         raise ValueError("Invalid Input! Please enter 'e/E' to encode or 'd/D' to decode.")
# except Exception as e:
#     print(e)

st = input("Enter Message : ")
words = st.split(" ")
coding = input("1 for Coding or 0 for Decoding")
coding=True if(coding=="1") else False
if(coding):
    nwords = []
    for word in words:
        if(len(word)>=3):
            r1 = "dsf"
            r2 = "jkr"
            stnew = r1+word[1:]+word[0]+r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords = []
    for word in words:
        if(len(word)>=3):
            stnew = word[3:-3]
            stnew = stnew[-1]+stnew[0:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))