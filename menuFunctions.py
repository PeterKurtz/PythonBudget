from DisplayMenu import *
from userInput import *
from tableSetup import *
from readingData import *
from datetime import date

editableArea = 40
bufferZone = 3

def chooseCategory(table, catName, title, description):
    choices = getTableChoices(table, catName)

    printChoices(title, description, editableArea, bufferZone, choices)

    userInput = getValidInt(len(choices))

    if userInput == 'b':
        return userInput
    
    catToBudget = choices[userInput - 1]

    catIDToBudget = getCatID(table, catName, catToBudget)

    return catIDToBudget

def printAndGetInt(title, description, maxNum):
    printChoices(title, description, editableArea, bufferZone)

    userInt = getValidInt(maxNum)

    return userInt

def printAndGetFloat(title, description):
    printChoices(title, description, editableArea, bufferZone)

    userInt = getValidFloat()

    return userInt

##################### Need to work on this
def printAndGetDate(title, description):
    printChoices(title, description, editableArea, bufferZone)

    userDate = input()

    return userDate

def printAndGetDescription(title, request):
    printChoices(title, request, editableArea, bufferZone)
    description = input()
    return description

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

            data = [nextID, catName, dateCreated]

            insertData(insertStatement, data)

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

def printMenu(title, request, choices):
    printChoices(title, request, editableArea, bufferZone, choices)

def createMenusAndProcess(title, catTable, catVariable, catRequest, tableToInsert):
    dataToInsert = []
    listOfMethods = [lambda: chooseCategory(catTable, catVariable, title, catRequest), 
                     lambda: printAndGetDescription(title, "Add a description"), 
                     lambda: printAndGetFloat(title, "Add a dollar amount"), 
                     lambda: printAndGetDate(title, "Add date")]
    
    processData(listOfMethods, tableToInsert)

def moneySpentOnBudget():
    createMenusAndProcess("Log Budget Spending", RegularCostCat, "CostCatName", "What budget category do you want to log?", RegularCosts)

def moneySpentOnSavings():
    createMenusAndProcess("Log Money Spent on Savings", SavingsCat, "SavingsCatName", "What savings category do you want to log?", IrregularCosts)

def addMoneySaved():
    createMenusAndProcess("Log Money Saved", SavingsCat, "SavingsCatName", "What savings category do you want to allocate money to?", Savings)

def updateBank():
    createMenusAndProcess("Update Total in Bank", BankCat, "BankName", "What bank category do you want to allocate money to?", BankBalance)

def addMoneyReceived():
    createMenusAndProcess("Add Money Received", PaymentCat, "PaymentName", "What money recieved category do you want to set?", Payments)



