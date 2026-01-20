import Platform
import OnExit
import Settings


def UserRoleMenu():
    print("1.Teacher\n2.Student\n0.Exit")
    userrole = Settings.get_int_in_range(2)
    return userrole



#Main
Settings.initialize()
while True:
    match UserRoleMenu():
        case 1:
            Platform.Teacher()
        case 2:
            Platform.Student()
        case 0:
            OnExit.On_Exit()
