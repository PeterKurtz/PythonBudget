def addSpaceAndBorders(statement, editableArea, bufferSpace):
    spacesToBuffer = ' '*bufferSpace

    numOfSpaces = editableArea-len(statement)
    spacesForStatement = ' '*numOfSpaces

    lineToPrint = '|' + spacesToBuffer + statement + spacesForStatement + spacesToBuffer + '|'

    return lineToPrint

def createRequest(request, editableArea, bufferSpace):
    requestLines = []
    requestCheck = request

    while len(requestCheck) > editableArea:
        indexToCheck = findIndex(requestCheck, editableArea)
        correctRequest = requestCheck[:indexToCheck]
        correctRequest = addSpaceAndBorders(correctRequest, editableArea, bufferSpace)
        requestLines.append(correctRequest)
        requestCheck = requestCheck[indexToCheck + 1:]
    requestCheck = addSpaceAndBorders(requestCheck, editableArea, bufferSpace)

    requestLines.append(requestCheck)

    return requestLines


def findIndex(request, indexToCheck):
    while request[indexToCheck] != ' ':
        indexToCheck = indexToCheck - 1

    return indexToCheck

def createChoices(choices, editableArea, bufferSpace):
    choicesLines = []

    for index, oneChoice in enumerate(choices):
        startOfChoice = True

        while len(oneChoice) > editableArea - 3:
            if startOfChoice == True:
                oneChoice = f'{index + 1}: {oneChoice}'
                startOfChoice = False

            else:
                oneChoice = f'   {oneChoice}'
            
            indexToCheck = findIndex(oneChoice, editableArea)
            correctChoice = oneChoice[:indexToCheck]
            correctChoice = addSpaceAndBorders(correctChoice, editableArea, bufferSpace)

            choicesLines.append(correctChoice)
            oneChoice = oneChoice[indexToCheck + 1:]

        oneChoice = addSpaceAndBorders(oneChoice, editableArea, bufferSpace)

        choicesLines.append(oneChoice)

    return choicesLines


def printChoices(title, request, editableArea, bufferSpace, choices = []):
    linesToPrint = []

    totalArea = editableArea + bufferSpace*2

    topAndBottomBorder = '+' + '='*totalArea + '+'
    fillerLayer = '|' + ' '*totalArea + '|'

    titleUnderline = title
    titleLine = addSpaceAndBorders(titleUnderline, editableArea, bufferSpace)
    linesToPrint = [topAndBottomBorder, fillerLayer, titleLine, fillerLayer]
    if len(request) > 0:
        requestLines = createRequest(request, editableArea, bufferSpace)
        linesToPrint += requestLines

    seperatorLine = addSpaceAndBorders('--', editableArea, bufferSpace)

    linesToPrint.append(seperatorLine)

    if len(choices) > 0:
        choicesLines = createChoices(choices, editableArea, bufferSpace)
        linesToPrint += choicesLines
        #print(choicesLines)

    for line in linesToPrint:
        print(line)

printChoices("test", "test is a test they are the people this is a long test", 20, 3, ["1st choice testing testing testing testing", "2nd Choice", "3rd Choice", "4th Choice"])
