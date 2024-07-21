# Questions = ["Who is the PM of India?", "Who was the first president of India?", "When did India get independent?"]
# Answers = ["Narendra Modi", "Rajendra Prasad", "1947"]
# Options = [["Rahul Gandhi", "Arvind Kejriwal", "Narendra Modi", "Mamta Banerjee"], 
#            ["Rajiv Gandhi", "Rajendra Prasad", "Jawahar Lal Nehru", "Indira Gandhi"], 
#            ["1950", "1956", "1949", "1947"]]

# amount = 0

# for i in range(len(Questions)):
#     print(Questions[i])
#     for j in range(len(Options[i])):
#         print(str(j + 1) + ". " + Options[i][j])

#     answer = input("Enter your response (1/2/3/4): ")
    
#     # Find the index of the correct answer manually
#     correct_answer_index = -1
#     for k in range(len(Options[i])):
#         if Options[i][k] == Answers[i]:
#             correct_answer_index = k + 1  # Indices for options are 1-based

#     if int(answer) == correct_answer_index:
#         amount += 1000
#         print("Congratulations! You have won", amount, "INR!")
#     else:
#         print("Wrong Answer!")
#         break  # Exit the loop if the answer is wrong

# print("You have won", amount, "INR!")

questions = [
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4
    ],
    [
        "Which language was used to create insta?", "Python", "French", "JavaScript", "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript", "Php", "None", 4
    ]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0


for i in range(0, len(questions)):
    question = questions[i]
    print(f"Question for Rs. {levels[i]}")
    print(f"{i+1}. {questions[i][0]}")
    print(f"a. {question[1]}            b. {question[2]}")
    print(f"c. {question[3]}        d. {question[4]}")
    reply = int(input("Enter your answer (1-4) or 0 to quit : \n"))
    if(reply == question[-1]):
        print(f"Correct Answer, You have won Rs. {levels[i]}\n")
        if(reply == 0):
            money = levels[i]
            break
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 10000000
    else:
        print("Wrong Answer!")
        break
print(f"Your take home money is {money}")