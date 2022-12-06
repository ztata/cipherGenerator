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
