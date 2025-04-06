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

    for line in linesToPrint:
        print(line)

printChoices("test", "test is a test they are the people this is a long test", 20, 3)