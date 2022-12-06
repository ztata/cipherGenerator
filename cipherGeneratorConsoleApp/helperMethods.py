def getValidSubKey() -> int:
    validNumber = False
    while validNumber == False:
        userInput = input("Please enter the substitution key for the message: ")
        if userInput.isnumeric() == False:
            print("Please enter a positive integer to continue")
            continue
        else:
            print("Thanks! Let's get to the message")
            validNumber = True
    return int(userInput)


def runSubstitutionAgain() -> bool:
    print("Would you like to encode or decode another message?")
    userInput = input("Enter y to repeat or anything else to quit: ")
    if userInput.strip().lower() == 'y':
        return True
    else:
        return False


def getValidKeyword(msg):
    msgLength = len(msg)
    print("Please come up with a keyword that is " + str(msgLength) + " characters long")
    print("If you word is too short, keep repeating the letters in order to reach the full length")
    validKey = False
    while validKey == False:
        userInput = input("Please enter your keyword: ")
        if len(userInput) > msgLength:
            print("Sorry, that keyword is " + str(len(userInput) - msgLength) + " too long")
            print("See if you can think of something a little shorter.")
            print(" ")
            continue
        elif len(userInput) < msgLength:
            print("Sorry, that keyword is " + str(msgLength - len(userInput)) + " too short")
            print("See if you can think of something a little longer.")
            print(" ")
            continue
        else:
            print("Thats perfect!")
            print(" ")
            validKey = True
    return userInput
            