import Quiz
import Settings

def Teacher():
    attempt = 0
    max_attempts = 3
    while attempt< 3:
        try:
            input_password = int(input("Enter password or 0 to exit\n"))
            if input_password == 1234:
                ShowTeacherMenu()
                TeacherMenuChoice()


            elif input_password == 0:
                break
            else:
                attempt +=1
                if max_attempts-attempt > 0:
                    print(f"Invalid password! Account will be lock after {max_attempts-attempt} times!")
        except:
            attempt += 1
            if max_attempts - attempt > 0:
                print(f"Invalid password! Account will be lock after {max_attempts - attempt} times!")
    if attempt >= max_attempts:
        print("Invalid password! Max attempts reached - Account Locked!")
        exit()


def ShowTeacherMenu():
    print("1.Edit Quiz\n2.Start Quiz\n3.View Score\n0.Quit")

def TeacherMenuChoice():

    # try:
        choice = Settings.get_int_in_range(3)
        match choice:
            case 1 :
                Quiz.Add()
            case 2:
                Quiz.Start()
            case 3:
                Quiz.ViewScore()
            case 0:
                return
            case _:
                print("Invalid input")
    # except:
    #     print("Invalid input")


def Student():
    # print("StudentPlatform")
    score = Quiz.Start()
    if score >= 70:
        print("Excellent!", end=" ")
    print(f"You {'pass' if score/len(Settings.global_QnA)*100>=40 else 'fail'} the quiz")