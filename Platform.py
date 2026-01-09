import Quiz

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
    print("1.Edit Quiz\n2.Start Quiz\n3. View Score\n0.Quit\n")

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