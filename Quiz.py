import Settings

def Add():

    while True:
        # try:
            print("1.Add Question\n2.View Question\n0.Return")
            choice = Settings.get_int_in_range(2)

            if choice == 1:
                inputQuestion = input("Enter question: ")
                Settings.global_QnA.append({"question":inputQuestion,"options":[],"answer":""})
                try:
                    num_of_options = int(input("Enter number of options: "))
                    if num_of_options <= 0:
                        print("Integer must be greater than 0")
                except:
                    print("Invalid input! Please enter a valid integer")
                for i in range(num_of_options):

                    option = option = input(f"Enter Option {i+1} of {num_of_options}: \nOption{chr(i+65)}: ")
                    Settings.global_QnA[-1]["options"].append(option)

                answer = input("Enter correct answer: ").upper()
                Settings.global_QnA[-1]["answer"] = answer
                print(Settings.global_QnA[-1])


                # try:
                #     inputQuestion = input("Enter question: ")
                #     inputOptionA = input("Enter Option A: ")
                #     inputOptionB = input("Enter Option B: ")
                #     inputOptionC = input("Enter Option C: ")
                #     inputOptionD = input("Enter Option D: ")
                #     while True:
                #         inputAnswer = input("Enter the correct answer: ").upper()
                #         if inputAnswer in ["A","B","C","D"]:
                #             break
                #         else:
                #             print(f"Invalid answer: {inputAnswer}")
                #     QnA ={"question": inputQuestion,
                #                "optionA": inputOptionA,
                #                "optionB": inputOptionB,
                #                "optionC": inputOptionC,
                #                "optionD": inputOptionD,
                #                "answer": inputAnswer}
                #     print(Settings.global_QnA)
                #     Settings.global_QnA.append(QnA)
                # print(Settings.global_QnA)
                # except:
                #     print("Unable to enter question")
            elif choice == 2:
                print("View Questions and Answer:")
                for i in range(0, len(Settings.global_QnA)):
                    # print(f"i = {i}")
                    print(f"\nQuestion{i+1}:", Settings.global_QnA[i]["question"])
                    for j in range(0,len(Settings.global_QnA[i]["options"])):
                        print(f"Option{chr(j+65)}: "+Settings.global_QnA[i]["options"][j])
                    print("Answer: "+str(Settings.global_QnA[i]["answer"]))
                # print(Settings.global_QnA)
                # print(Settings.global_QnA[0])
                # print(Settings.global_QnA[0]["question"])
                # print(Settings.global_QnA[0]["question"],Settings.global_QnA[0]["optionA"])
                # print("Question: ", Settings.global_QnA[0]["question"])

            elif choice == 0:
               break
        # except:
        #     print("Invalid input")

# def ViewQuestion():
#     print("ViewQuestion")

    # for i in

def Start():
    print("Start quiz")
    while True:
        try:
            input_ID = int(input("Enter your Student_ID: "))
            break
        except:
            print("Invalid input! Please enter your ID again")
    score = 0

    for i in range(0,len(Settings.global_QnA)):
        # print(f"score: {score}")
        # print(f"i = {i}")
        print(f"Question{i + 1}:", Settings.global_QnA[i]["question"])
        for j in range(0, len(Settings.global_QnA[i]["options"])):
            print(f"Option{chr(j + 65)}: " + Settings.global_QnA[i]["options"][j])
        while True:
            try:
                student_answer = input("Enter your answer in Alphabet: ").upper()
                # print(len(Settings.global_QnA[i]["options"])+65)
                # print(ord(student_answer))
                # print(Settings.global_QnA[i]["answer"])
                # print(Settings.global_QnA[i]["options"][ord(student_answer)-65])
                if not 65<= ord(student_answer) <=len(Settings.global_QnA[i]["options"])+65:
                    print("Invalid answer!")
                if str(Settings.global_QnA[i]["answer"]) == str(Settings.global_QnA[i]["options"][ord(student_answer)-65]):
                    score += 1
                    print("Correct!")
                    print(f"Score: {score}")
                    break
                else:
                    print("Incorrect! The correct answer is: "+str(Settings.global_QnA[i]["answer"]))
                    break
                    # print(f"score: {score}")
            except:
                print("Incorrect! The correct answer is: "+str(Settings.global_QnA[i]["answer"]))
                break


    print(f"Quiz Finished!\nYour final score is {score}/ {len(Settings.global_QnA)} = {score/len(Settings.global_QnA)*100}%")
    # print(input_ID)
    # print(score)
    Settings.students.append({'studentID':input_ID, 'studentScore':score})
    # print(Settings.students)
    return score

def ViewScore():
    # print("ViewScore")
    for i in range (0,len(Settings.students)):
        # print(f"i = {i}")
        print(f"Student_ID: "+ str(Settings.students[i]["studentID"]))
        print(f"Score: "+str(Settings.students[i]["studentScore"])+"/"+str(len(Settings.global_QnA)))
        Settings.total_score += Settings.students[i]["studentScore"]
        if(Settings.students[i]["studentScore"])/len(Settings.global_QnA)*100 >= 40:
            Settings.num_of_pass +=1
        if Settings.students[i]["studentScore"]/len(Settings.global_QnA)*100 >= 70:
            Settings.num_of_distinction +=1
    print(f"Total of test taken: {len(Settings.students)}")
    print(f"Average: {Settings.total_score/len(Settings.students)}")
    print(f"Number of fail: {len(Settings.students)-Settings.num_of_pass}")
    print(f"Number of pass: {Settings.num_of_pass}")
    print(f"Number of distinction: {Settings.num_of_distinction}")

