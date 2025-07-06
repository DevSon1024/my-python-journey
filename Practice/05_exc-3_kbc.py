questions = [
    ["Which language was used to create fb?","French","PHP","Javascript","None",4],
    ["Which language was used to create fb?","Python","PHP","Javascript","None",3],
    ["Which language was used to create fb?","Python","French","Javascript","None",2],
    ["Which language was used to create fb?","Python","French","Javascript","None",3],
    ["Which language was used to create fb?","Python","French","PHP","None",4]
]

levels = [1000,2000,3000,5000,10000,50000,80000,100000]

money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\nQuestions for Rs. {levels[i]}")
    print(f"a. {question[1]}             b.{question[2]}")
    print(f"c. {question[3]}             d.{question[4]}")
    
    reply = int(input("Enter Your Answer (1-4) 0 to quit: \n"))
    if reply == 0:
        money = levels[i-1]
        break
    if reply == question[-1]:
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if i == 4:
            money = 10000
        elif i == 9:
            money == 320000
        elif i == 14:
            money = 140000
    else:
        print("Wrong Answer!")
        break

print(f"Your Take home money is {money}")
