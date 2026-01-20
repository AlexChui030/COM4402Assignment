
import Platform
import OnExit
import Settings



# def initialize():
#     global global_QnA, score, studentAnswer
#     global_QnA = [1,0]
#     print(global_QnA)
#     score = {
#         "studentID": None,
#         "studentScore": None,
#     }
#
#     studentAnswer = []

    # return quiz_QnA, score, studentAnswer

def UserRoleMenu():
    print("1.Teacher\n2.Student\n0.Exit")
    userrole = Settings.get_int_in_range(2)
    return userrole


###########################################################################
#Main
# quiz_QnA, score, studentAnswer = initialize()
Settings.initialize()
# print (Settings.ttt)
# Settings.ttt = "AAA"
# print (Settings.ttt)
# alist = Settings.global_QnA
# print (alist)
# alist.append(2)
# print(alist)
# print(Settings.global_QnA)
# Settings.global_QnA.append(1)
# print(Settings.global_QnA)
## Settings.global_QnA = alist
## print(Settings.global_QnA)
## print (list(Settings.global_QnA).append(5))
# QnA ={"question": "A1","optionA": "1","optionB": "2","optionC": "3","optionD": "4","answer": "A"}
# Settings.global_QnA.append(QnA)
# print(Settings.global_QnA)
# QnA ={"question": "B2","optionA": "1","optionB": "2","optionC": "3","optionD": "4","answer": "B"}
# Settings.global_QnA.append(QnA)
# print(Settings.global_QnA)
while True:
    match UserRoleMenu():
        case 1:
            Platform.Teacher()
        case 2:
            Platform.Student()
        case 0:
            OnExit.On_Exit()

# question ={"question": "inputQuestion",
#                                "optionA": "inputOptionA",
#                                "optionB": "inputOptionB",
#                                "optionC": "inputOptionC",
#                                "optionD": "inputOptionD",
#                                "answer": "A"}
# quiz_QnA.append(question)
# print(quiz_QnA)
# print(quiz_QnA[0]["optionA"])