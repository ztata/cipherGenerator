
def readFromFile():
    file = open("cipherInput.txt", "r")
    msg = file.read()
    file.close()
    return msg


def writeToFile(msg):
    file = open("cipherOutput.txt", "w")
    file.write(msg)
    file.close()


def encodeTextFile():
    msg = readFromFile()
    #This doesnt encode anything yet
    #put options here on how you would like the mesaage to be encoded 
    #need to have them enter the sub key or keyword as well then call on the methods from the other
    #files and write that here 
    writeToFile(msg)
    print("Message encoded, results are available in the output file")