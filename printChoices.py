def addSpaceAndBorders(statement, editableArea, bufferSpace):
    spacesToBuffer = ' '*bufferSpace

    numOfSpaces = editableArea-len(statement)
    spacesForStatement = ' '*numOfSpaces

    lineToPrint = '|' + spacesToBuffer + statement + spacesForStatement + spacesToBuffer + '|'

    return lineToPrint




def printChoices(title, request, editableArea, bufferSpace, choices = []):
    linesToPrint = []

    totalArea = editableArea + bufferSpace

    topAnBottomBorder = '+' + '='*totalArea + '+'
    fillerLayer = '|' + ' '*totalArea + '|'

    titleUnderline = title
    titleLine = addSpaceAndBorders(titleUnderline, editableArea, bufferSpace)
    linesToPrint = [topAnBottomBorder, fillerLayer, titleLine, fillerLayer]
    print(linesToPrint)

print(printChoices("", "", 3, 3))