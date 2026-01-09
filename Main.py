import Platform
import OnExit



def initialize():
    question = {
        "qustionNo": None,
        "question": None,
        "answer": None
    }

    score = {
        "studentID": None,
        "studentScore": None,
    }

    studentAnswer = []


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
initialize()
while True:
    match UserRoleMenu():
        case 1:
            Platform.Teacher()

        case 2:
            Platform.Student()

        case 0:
            OnExit.On_Exit()
############################################################################
