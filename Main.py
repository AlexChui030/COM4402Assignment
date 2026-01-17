import Platform
import OnExit



def initialize():
    quiz_QnA = []
    score = {
        "studentID": None,
        "studentScore": None,
    }

    studentAnswer = []

    return quiz_QnA, score, studentAnswer

def UserRoleMenu():
    userrole = None
    try :
        userrole = int(input("1.Teacher\n2.Student\n0.Exit\n"))
        if userrole not in [0,1,2]:
            print("input 1 or 2, or 0 to exit")

    except:
        print("input 1 or 2, or 0 to exit")
    return userrole


###########################################################################
#Main
quiz_QnA, score, studentAnswer = initialize()
while True:
    match UserRoleMenu():
        case 1:
            Platform.Teacher(quiz_QnA)
        case 2:
            Platform.Student(quiz_QnA, score, studentAnswer)

        case 0:
            OnExit.On_Exit()
############################################################################
