import passwordIO
import randomPasswordGenerator


def generatedRoutine():
    print("======================== Welcome to the Password Generator ========================")
    print("Please choose your option:")
    print("1 - Create Password")
    print("2 - View Password")
    print("3 - Delete Password")
    print("4 - Exit")
    userInput = int(input())
    if userInput == 1:
        createPassword()
    elif userInput == 2:
        viewPasswords()
    elif userInput == 3:
        deletePasswords()
    elif userInput == 4:
        exit(1)
    else:
        generatedRoutine()


def createPassword():
    service = input("What service is the password for? ")
    passwordLength = None
    try:
        passwordLength = int(input("How long should the password be? "))
    except ValueError:
        print("Please only input numbers!!")
        createPassword()
        exit(1)
    generatedPassword = randomPasswordGenerator.generatePassword(passwordLength)
    cleanPassword = ""
    for n in range(0, len(generatedPassword)):
        cleanPassword += str(generatedPassword[n])
    print(service, cleanPassword)
    passwordIO.writingPassword(service, cleanPassword)
    generatedRoutine()


def viewPasswords():
    listPasswordsFinal = passwordIO.readingPassword()
    for items in range(0, len(listPasswordsFinal)):
        print(items, listPasswordsFinal[items])
    generatedRoutine()


def deletePasswords():
    viewPasswords()
    index = input("What index would you like to delete?")
    passwordIO.deletingPassword(int(index))
    generatedRoutine()
