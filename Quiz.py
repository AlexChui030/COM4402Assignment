def Edit():
    while True:
        try:
            choice = int(input("1.Add Question\n0.Return"))
            if choice not in [0,1]:
                print("Invalid input")
            elif choice == 1:
                try:
                    inputQuestion = input("Enter question")
                    inputOptionA = input("Enter Option A")
                    inputOptionB = input("Enter Option B")
                    inputOptionC = input("Enter Option C")
                    inputOptionD = input("Enter Option D")
                    inputAnswer = input("Enter the correct answer")
                    inputQuestionTuple = (inputQuestion,inputOptionA,inputOptionB,inputOptionC,inputOptionD)


                except:
                    print("Unable to enter question")
            elif choice == 0:
               break
        except:
            print("Invalid input")

def Start():
    print()

def ViewScore():
    print()