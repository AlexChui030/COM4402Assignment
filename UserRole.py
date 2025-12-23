def menu():
    userrole = None
    try :
        userrole = int(input("1.Teacher \n2.Student\n"))
        if userrole not in [1,2]:
            print("input 1 or 2")

    except:
        print("input 1 or 2")
    return userrole