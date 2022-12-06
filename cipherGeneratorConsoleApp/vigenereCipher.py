import string
import helperMethods
import os

def checkIfItWorks():
    print("You made it to the vigenere cipher file")



def runVigenereCipher():
    runAgain = True
    while runAgain:
      print("Would you like to encode or decode a message?")
      userInput = input("Enter E for encode or anything else to decode a message: ")
      if userInput.lower().strip() == 'e':
        print(" ")
        msg = input("Please enter the message you would like to encode: ")
        keyword = helperMethods.getValidKeyword(msg)
        encode(msg, keyword)
      else:
        print(" ")
        msg = input("Please enter the message you would like to decode: ")
        keyword = helperMethods.getValidKeyword(msg)
        decode(msg, keyword)
      runAgain = helperMethods.runSubstitutionAgain()
      os.system('cls')






def encode(msg: string, keyword: string):
    keyArray = []
    letters = list(string.ascii_lowercase)
    encodedMsg = ""
    for char in keyword.strip().lower():
        index = letters.index(char)
        keyArray.append(index+1)
    counter = 0
    for char in msg.strip().lower():
        index = letters.index(char)
        index += keyArray[counter]
        counter += 1
        newChar = letters[index % len(letters)]
        encodedMsg += newChar
    print("Encoded Message: " + encodedMsg)

def decode(msg: string, keyword: string):
  keyArray = []
  letters = list(string.ascii_lowercase)
  decodedMsg = ""
  for char in keyword.strip().lower():
    index = letters.index(char)
    keyArray.append(index+1)
  counter = 0
  for char in msg.strip().lower():
      index = letters.index(char)
      index -= keyArray[counter]
      counter += 1
      newChar = letters[index % len(letters)]
      decodedMsg += newChar
  print("Decoded Message: " + decodedMsg)