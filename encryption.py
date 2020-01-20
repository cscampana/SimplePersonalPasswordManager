from cryptography.fernet import Fernet

key = "Hello Github"  # create your own personal key


def encrypted(cleanString):
    f = Fernet(key)
    token = f.encrypt(cleanString)
    return token


def decrypted(token):
    f = Fernet(key)
    passwordInfo = f.decrypt(token)
    return passwordInfo
