import UserRole
import Platform
import initialize

initialize.initialize()


while True:
    match UserRole.menu():
        case 1:
            Platform.Teacher()

        case 2:
            Platform.Student()

