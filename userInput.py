def getValidInt(maxNum):
    continueLoop = True
    while continueLoop:
        try:
            userInput = input()
            if userInput == 'b':
                return userInput
            userInputInt = int(userInput)
            if 1 <= userInputInt <= maxNum:
                continueLoop = False
            else:
                raise
        except:
            print("Incorrect Input")
    return userInputInt

print(getValidInt(3))