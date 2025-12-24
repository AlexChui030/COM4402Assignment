import Quiz


def Teacher():
    while True:
        try:
            inputpassword = int(input("Enter password or 0 to exit\n"))
            if inputpassword == 1234:
                ShowTeacherMenu()
                TeacherMenuChoice()
                break
            elif inputpassword == 0:
                break
            else:
                print("Invalid password")
        except:
            print("Invalid password")




def ShowTeacherMenu():
    print("1. View/ Edit Quiz\n2.Start Quiz\n3. View Score\n0.Quit\n")

def TeacherMenuChoice():
    try:
        choice = int(input())
        match choice:
            case 1 :
                Quiz.Edit()
            case 2:
                Quiz.Start()
            case 3:
                Quiz.ViewScore()
            case 0:
                return
            case _:
                print("Invalid input")
    except:
        print("Invalid input")


def Student():
    print("StudentPlatform")