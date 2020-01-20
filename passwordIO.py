import encryption


def writingPassword(service, passwordTobeWritten):
    outPutFile = open("passwords.cry", "ab")
    final = f"{service}: {passwordTobeWritten}"
    finalBytes = bytes(final, 'utf-8')
    token = encryption.encrypted(finalBytes)
    outPutFile.write(token)
    outPutFile.write(bytes("********", 'utf-8'))


def readingPassword():
    inputFile = open("passwords.cry", "rb")
    line = inputFile.readlines()
    lineB = str(line).strip("[b'")
    listPasswords = lineB.split("********")
    listPasswordsFinal = []
    for item in range(0, len(listPasswords) - 1):
        tempStr = str(encryption.decrypted(bytes(listPasswords[item], "utf-8")))
        tempStr = tempStr.strip("b'")
        tempStr = tempStr.strip("'")
        listPasswordsFinal.append(tempStr)
    inputFile.close()
    return listPasswordsFinal


def deletingPassword(index):
    listPasswords = readingPassword()
    del listPasswords[index]
    outPutFile = open("passwords.cry", "wb")
    for items in range(0, len(listPasswords)):
        finalBytes = bytes(listPasswords[items], 'utf-8')
        token = encryption.encrypted(finalBytes)
        outPutFile.write(token)
        outPutFile.write(bytes("********", 'utf-8'))
