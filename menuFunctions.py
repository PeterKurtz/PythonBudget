from DisplayMenu import *
from userInput import *
from tableSetup import *
from readingData import *

editableArea = 40
bufferZone = 3

def chooseCategory(table, catName, title, description):
    choices = getTableChoices(table, catName)

    printChoices(title, description, editableArea, bufferZone, choices)

    userInput = getValidInt(len(choices))

    if userInput == 'b':
        return userInput
    
    catToBudget = choices[userInput - 1]

    catIDToBudget = getCatID(RegularCostCat, catToBudget)

    return catIDToBudget

def printAndGetInt(title, description, maxNum):
    printChoices(title, description, editableArea, bufferZone)

    userInt = getValidInt(maxNum)

    return userInt

def printAndGetFloat(title, description):
    printChoices(title, description, editableArea, bufferZone)

    userInt = getValidFloat()

    return userInt

def showCategories(table):
    title = f"Categories for:"
    request = table.get_name()
    choices = getTableChoices(table, table.columnArray[1].get_name())
    printChoices(title, request, editableArea, bufferZone, choices)
    input()

def insertCategory(table, title):
    fullTitle = f"{title} Category"

    while True:

        request = "What is the name of the new category? Select s if you would like to see the current categories."
        printChoices(fullTitle, request, editableArea, bufferZone)

        catName = input()

        if catName == 'b':
            return catName
        
        elif catName == 's':
            showCategories(table)
        
        else:
            insertStatement = table.createInsertString()

            nextID = getNextID(table)
            dateCreated = date.today()

            con = sqlite3.connect("budget.db")
            cur = con.cursor()

            data = [nextID, catName, dateCreated]

            cur.execute(insertStatement, data)

            con.commit()
            con.close()

            return "not finished"
        
def collectData(listOfMethods):

    dataToInsert = []
    indexOfMethods = 0
    lastMethodIndex = len(listOfMethods) - 1

    while indexOfMethods <= lastMethodIndex:
        userInput = listOfMethods[indexOfMethods]()
        if userInput == 'b' and indexOfMethods == 0:
            return dataToInsert
        elif userInput == 'b' and indexOfMethods > 0:
            indexOfMethods -= 1
            dataToInsert = dataToInsert[:indexOfMethods]
        else:
            dataToInsert.append(userInput)
            indexOfMethods += 1

    return dataToInsert

def insertData(insertString, data):

    con = sqlite3.connect("budget.db")
    cur = con.cursor()

    cur.execute(insertString, data)
    con.commit()

    con.close()

def processData(listOfMethods, table):
    dataToInsert = collectData(listOfMethods)

    if len(dataToInsert) == 0:
        return

    sqlInsert = table.createInsertString()
    insertData(sqlInsert, dataToInsert)