import Settings

def Add():

    while True:
        # try:
            choice = int(input("1.Add Question\n2.View Question\n0.Return\n"))
            if choice not in [0,1,2]:
                print("Invalid input")
            elif choice == 1:
                # try:
                    inputQuestion = input("Enter question: ")
                    inputOptionA = input("Enter Option A: ")
                    inputOptionB = input("Enter Option B: ")
                    inputOptionC = input("Enter Option C: ")
                    inputOptionD = input("Enter Option D: ")
                    while True:
                        inputAnswer = input("Enter the correct answer: ").upper()
                        if inputAnswer in ["A","B","C","D"]:
                            break
                        else:
                            print(f"Invalid answer: {inputAnswer}")
                    QnA ={"question": inputQuestion,
                               "optionA": inputOptionA,
                               "optionB": inputOptionB,
                               "optionC": inputOptionC,
                               "optionD": inputOptionD,
                               "answer": inputAnswer}
                    print(Settings.global_QnA)
                    Settings.global_QnA.append(QnA)
                    print(Settings.global_QnA)
                # except:
                #     print("Unable to enter question")
            elif choice == 2:
                print("View Questions and Answer:")
                for i in range(0, len(Settings.global_QnA)):
                    print(f"i = {i}")
                    print(f"Question{i+1}:", Settings.global_QnA[i]["question"],"\n    OptionA: "+
                          Settings.global_QnA[i]["optionA"],"\n    OptionB: "+
                          Settings.global_QnA[i]["optionB"],"\n    OptionC: "+
                          Settings.global_QnA[i]["optionC"],"\n    OptionD: "+
                          Settings.global_QnA[i]["optionD"],"\n    Answer : "+
                          Settings.global_QnA[i]["answer"])
                # print(Settings.global_QnA)
                # print(Settings.global_QnA[0])
                # print(Settings.global_QnA[0]["question"])
                # print(Settings.global_QnA[0]["question"],Settings.global_QnA[0]["optionA"])
                # print("Question: ", Settings.global_QnA[0]["question"])

            elif choice == 0:
               break
        # except:
        #     print("Invalid input")

def ViewQuestion():
    print("ViewQuestion")

    # for i in

def Start():
    print("Start quiz")
    input_ID = int(input("Enter your Student_ID: "))
    score = 0

    for i in range(0,len(Settings.global_QnA)):
        # print(f"score: {score}")
        print(f"i = {i}")
        print(f"Question{i + 1}:", Settings.global_QnA[i]["question"], "\n    OptionA: " +
              Settings.global_QnA[i]["optionA"], "\n    OptionB: " +
              Settings.global_QnA[i]["optionB"], "\n    OptionC: " +
              Settings.global_QnA[i]["optionC"], "\n    OptionD: " +
              Settings.global_QnA[i]["optionD"])
        while True:
            student_answer = input("Enter your answer: ").upper()
            if student_answer in ["A","B","C","D"]:
                break
            else:
                print("Invalid answer! Input again")
        if student_answer == Settings.global_QnA[i]["answer"]:
            score += 1
            print("Correct!")
            print(f"Score: {score}")
        else:
            print("Incorrect! The correct answer is: "+Settings.global_QnA[i]["answer"])
            # print(f"score: {score}")
            break
    print(f"Quiz Finished!\nYour final score is {score}")
    Settings.students.append({input_ID : score})
    print(Settings.students)


def ViewScore():
    print("ViewScore")
    for i in range (0,len(Settings.students)):
        print(f"i = {i}")
        print(f"Student_ID: "+ str(Settings.students[i]["studentID"]))
        print(f"Score: "+str(Settings.students[i]["studentScore"]))
        Settings.total_score += Settings.students[i]["studentScore"]
        if Settings.students[i]["studentScore"] >= 40:
            Settings.num_of_pass +=1
        if Settings.students[i]["studentScore"] >= 70:
            Settings.num_of_distinction +=1
    print(f"Total: {len(Settings.students)}")
    print(f"Average: {Settings.total_score/len(Settings.students)}")
    print(f"Number of fail: {len(Settings.students)-Settings.num_of_pass}")
    print(f"Number of pass: {Settings.num_of_pass}")
    print(f"Number of distinction: {Settings.num_of_distinction}")

