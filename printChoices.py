def addSpaceAndBorders(statement, editableArea, bufferSpace):
    spacesToBuffer = ' '*bufferSpace

    numOfSpaces = editableArea-len(statement)
    spacesForStatement = ' '*numOfSpaces

    lineToPrint = '|' + spacesToBuffer + statement + spacesForStatement + spacesToBuffer + '|'

    return lineToPrint




def printChoices(title, request, editableArea, bufferSpace, choices = []):
    linesToPrint = []

    totalArea = editableArea + bufferSpace

    topAndBottomBorder = '+' + '='*totalArea + '+'
    fillerLayer = '|' + ' '*totalArea + '|'

    titleUnderline = title
    titleLine = addSpaceAndBorders(titleUnderline, editableArea, bufferSpace)
    linesToPrint = [topAndBottomBorder, fillerLayer, titleLine, fillerLayer]
    for line in linesToPrint:
        print(line)

printChoices("test", "test", 40, 3)