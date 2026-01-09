

def Edit():
    while True:
        try:
            choice = int(input("1.Add Question\n2.View Question\n0.Return\n"))
            if choice not in [0,1]:
                print("Invalid input")
            elif choice == 1:
                try:
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
                    QuestionTuple = (inputQuestion,inputOptionA,inputOptionB,inputOptionC,inputOptionD,inputAnswer)

                except:
                    print("Unable to enter question")
            elif choice ==2:
                ViewQuestion()
            elif choice == 0:
               break
        except:
            print("Invalid input")

def ViewQuestion():
    print("ViewQuestion")
    # for i in

def Start():
    print("Start quiz")

def ViewScore():
    print("ViewScore")


