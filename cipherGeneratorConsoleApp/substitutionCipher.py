import helperMethods
import os


def checkIfItWorks():
    print("You made it to the substitution cipher file")



def runSubstitutionCipher():
    runAgain = True
    while runAgain:
      print("Would you like to encode or decode a message?")
      userInput = input("Enter E for encode or anything else to decode a message: ")
      if userInput.lower().strip() == 'e':
        subKey = helperMethods.getValidSubKey()
        message = input("Please enter the message you would like to encode: ")
        encode(subKey, message)
      else:
        subKey = helperMethods.getValidSubKey()
        message = input("Please enter the message you would like to decode: ")
        decode(subKey, message)
      runAgain = helperMethods.runSubstitutionAgain()
      os.system('cls')
      



def encode(subKey: int, msg: str):
    print(" ")
    print("Substitution Key: " + str(subKey))
    print("Message to be decoded: " + msg)
    print(" ")
    encodedMessage = ""
    numsList = [*range(32,127)]
    for char in msg:
        charNum = ord(char)
        index = numsList.index(charNum)
        index = index + subKey       
        newCharNum = numsList[index % len(numsList)]
        newChar = chr(newCharNum)
        encodedMessage += newChar
    print("Encoded message: " + encodedMessage)

def encodeForFile(subKey: int, msg: str):
    encodedMessage = ""
    numsList = [*range(32,127)]
    for char in msg:
        charNum = ord(char)
        index = numsList.index(charNum)
        index = index + subKey       
        newCharNum = numsList[index % len(numsList)]
        newChar = chr(newCharNum)
        encodedMessage += newChar
    return encodedMessage

def decode(subKey: int, msg: str):
    print(" ")
    print("Substitution Key: " + str(subKey))
    print("Message to be decoded: " + msg)
    print(" ")
    decodedMessage = ""
    numsList = [*range(32,127)]
    for char in msg:
        charNum = ord(char)
        index = numsList.index(charNum)
        index -= subKey
        newCharNum = numsList[index % len(numsList)]
        newChar = chr(newCharNum)
        decodedMessage += newChar
    print("Decrypted message: " + decodedMessage)
    print(" ")