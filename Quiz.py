import Settings

def Add():

    while True:

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
                    print("Please enter a valid integer")
                for i in range(num_of_options):

                    option = input(f"Enter Option {i+1} of {num_of_options}: \nOption{chr(i+65)}: ")
                    Settings.global_QnA[-1]["options"].append(option)

                answer = input("Enter correct answer: ").upper()
                Settings.global_QnA[-1]["answer"] = answer
                print(Settings.global_QnA[-1])

            elif choice == 2:
                print("View Questions and Answer:")
                for i in range(0, len(Settings.global_QnA)):
                    # print(f"i = {i}")
                    print(f"\nQuestion{i+1}:", Settings.global_QnA[i]["question"])
                    for j in range(0,len(Settings.global_QnA[i]["options"])):
                        print(f"Option{chr(j+65)}: "+Settings.global_QnA[i]["options"][j])
                    print("Answer: "+str(Settings.global_QnA[i]["answer"]))

            elif choice == 0:
               break

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
        print(f"Question{i + 1}:", Settings.global_QnA[i]["question"])

        for j in range(0, len(Settings.global_QnA[i]["options"])):
            print(f"Option{chr(j + 65)}: " + Settings.global_QnA[i]["options"][j])

        while True:
            try:
                student_answer = input("Enter your answer in Alphabet: ").upper()

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

            except:
                print("Incorrect! The correct answer is: "+str(Settings.global_QnA[i]["answer"]))
                break


    print(f"Quiz Finished!\nYour final score is {score}/ {len(Settings.global_QnA)} = {score/len(Settings.global_QnA)*100}%")
    Settings.students.append({'studentID':input_ID, 'studentScore':score})
    return score

def ViewScore():
    print("*************************************************")
    for i in range (0,len(Settings.students)):
        print(f"Student_ID: "+ str(Settings.students[i]["studentID"]))
        print(f"Score: "+str(Settings.students[i]["studentScore"])+"/"+str(len(Settings.global_QnA)))
        Settings.total_score += Settings.students[i]["studentScore"]

        if(Settings.students[i]["studentScore"])/len(Settings.global_QnA)*100 >= 40:
            Settings.num_of_pass +=1

        if Settings.students[i]["studentScore"]/len(Settings.global_QnA)*100 >= 70:
            Settings.num_of_distinction +=1
        print("*************************************************")
    print(f"Total of test taken: {len(Settings.students)}")
    print(f"Average: {Settings.total_score/len(Settings.students)}")
    print(f"Number of fail: {len(Settings.students)-Settings.num_of_pass}")
    print(f"Number of pass: {Settings.num_of_pass}")
    print(f"Number of distinction: {Settings.num_of_distinction}")

