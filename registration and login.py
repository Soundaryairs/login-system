def register():
    db = open("access_register.txt", "r")
    a = input("Create your Email ID: ")
    d = []
    for line in db:
        x = line.split(",")
        d.append(x[0])

    if a in d:
        print("Try Again with different Email ID")
        register()

    elif a.count('@') != 1 and a.count('.') != 1:
        print("Invalid format")
        register()

    elif ((a.index('@')) - (a.index('.'))) == 1:
        print("Invalid format")
        register()

    elif a[0] in range(0, 9):
        print("Beginning of your Email ID cannot be a Number")
        register()

    elif (a[0] == '@' or a[0] == '$' or a[0] == '_' or a[0] == '%' or a[0] == '!' or a[0] == '#' or a[0] == '*' or a[
        0] == '&'):
        print("Beginning of your Email ID cannot be special characters")
        register()

    else:
        print("Email ID created successfully")

    b = input("Create your password with atleast one capital letter one integer and one special character: ")
    s = False

    if len(b) < 5 and len(b) > 16:
        print("Password length should be atlest between 5 to 16 characters ,Please Try Again")
        register()

    if len(b) > 5 and len(b) < 16:
        l, u, p, d = 0, 0, 0, 0
        for i in b:
            if i.isdigit():
                d += 1
            if i.islower():
                l += 1
            if i.isupper():
                u += 1
            if (i == '@' or i == '$' or i == '_' or i == '%' or i == '!' or i == '#' or i == '*' or i == '&'):
                p += 1
            if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(b)):
                s = True

    if s:
        c = input("Confirm Password: ")
        while (c != b):
            print("Password does not match, Try Again")
            c = input("Try Again: ")

    else:
        print("Try again")
        register()

    file = open("access_register.txt", "a")
    file.write(a + "," + b + "\n")
    file.close()
    print(" Your Account created successfully")


def login():
    X=input("Enter your Email ID to login: ")
    X = X.strip()
    db = open("access_register.txt", "r")
    d = []
    for line in db:
        x = line.split(",")
        d.append(x[0])

    if X in d:
        Y=input(" Enter your password: ")
        Y=Y.strip()
        file1=open("access_register.txt","r").readlines()
        for x in file1:
            x=x.strip()
            info=x.split(",")
            if X==info[0] and Y==info[1]:
                print(f" your Loggin is successfull, Welcome {X}")
                exit()



            else:
                F = input("Forgot Password [Y/N] : ")

                if F == "N":
                    print("try again")
                    login()

                if F == "Y":
                    b = input("Create your new password with atleast one capital letter one integer and one special character: ")
                    s = False

                    if len(b) < 5 and len(b) > 16:
                        print("Create Password with length between 5 an 16, Try Again")
                        register()

                    if len(b) > 5 and len(b) < 16:
                        l, u, p, d = 0, 0, 0, 0
                        for i in b:
                            if i.isdigit():
                                d += 1
                            if i.islower():
                                l += 1
                            if i.isupper():
                                u += 1
                            if (i == '@' or i == '$' or i == '_' or i == '%' or i == '!' or i == '#' or i == '*' or i == '&'):
                                p += 1
                            if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(b)):
                                s = True

                        if s:
                            c = input("Confirm Password: ")
                            while (c != b):
                                print("Password does not match, Try Again")
                                c = input("Try Again: ")

                        else:
                            print("Sorry,Try again to login")
                            login()

                        file = open("access_register.txt", "w")
                        file.write(X + "," + b + "\n")
                        file.close()

    else:
        print("You have not Registered")
        register()

def welcome():
    print("WELCOME, Press L to Login and if you are a new user then press R to register")
    W=input("Login|Register[L/R]: ")
    if W=="L":
        login()
    elif W=="R":
        register()
    else:
        print("Please do enter the credentials properly")
        welcome()
welcome()