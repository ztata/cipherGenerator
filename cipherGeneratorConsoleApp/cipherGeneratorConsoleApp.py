import os
import substitutionCipher
import vigenereCipher

os.system('cls')
repeat = True
while repeat:
    print("Welcome to the cipher generation app")
    userName = input("Please enter your name: ")
    print("Hi, " + userName + "!")
    print("-----------------------------------------------------------")
    print("Cipher Types:")
    print("1). Substitution Cipher")
    print("2). Vigenere Cipher")
    validInput = False
    userInput = ""
    while validInput == False:
        userInput = input("Please enter the number of the cipher you would like to use: ")
        if userInput.isnumeric() == False or int(userInput) < 1 or int(userInput) > 2:
            print("Please enter one of the numbers listed above")
            continue
        else:
            print("Thanks! Let's get started.")
            validInput = True
            os.system('cls')
    if userInput == "1":
        substitutionCipher.runSubstitutionCipher()
    else:
        vigenereCipher.checkIfItWorks()

    print("Thats the end of what we have at present ")


    #Make this into a separate method later on
    print("Would you like to run the program again?")
    userInput = input("Enter Y to do so, or anything else to quit: ")
    if userInput.lower().strip() == 'y':
        repeat = True
    else:
        repeat = False

print("Thanks for checking out this project!")
      






        