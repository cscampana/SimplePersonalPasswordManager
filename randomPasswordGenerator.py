import random


def generatePassword(length):
    passwordGenerated = []
    for i in range(0, length):
        num = random.randint(46, 124)
        if (num % 2) == 0 or (num % 3) == 0:
            passwordGenerated.append(chr(num))
        else:
            passwordGenerated.append(random.randint(0, 9))
    return passwordGenerated
