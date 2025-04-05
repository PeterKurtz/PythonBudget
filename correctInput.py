def checkNumIsValid(userNum, maxNum):
    correctInput = True

    return correctInput

def getUserNumData(numOfChoices):
    choiceIsValid = False
    while choiceIsValid == False:
        userChoiceNum = input()
        if userChoiceNum == 'b':
            return userChoiceNum
        choiceIsValid = checkNumIsValid(userChoiceNum, numOfChoices)
        if choiceIsValid == False:
            print("Invalid Input")
    return userChoiceNum

x = getUserNumData(3)
print(x)
