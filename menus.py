from DisplayMenu import *
from userInput import *
from tableSetup import *
from datetime import date
import sqlite3

editableArea = 40
bufferZone = 3

def moneyInOut():
    print("Went to moneyInOut")

def getTableChoices(table, catName):
    con = sqlite3.connect("budget.db")
    cur = con.cursor()

    sqlString = f"SELECT {catName} FROM {table.get_name()}"

    result = cur.execute(sqlString).fetchall()
    categories = []
    for cat in result:
        categories.append(cat[0])
    #Eventually put in code to check if anything is there, for now we will assume category stuff has been set up

    con.close()

    return categories


def chooseCategory(table, catName, title, description):
    choices = getTableChoices(table, catName)

    printChoices(title, description, editableArea, bufferZone, choices)

    userInput = getValidInt(len(choices))

    if userInput == 'b':
        return userInput
    
    catToBudget = choices[userInput - 1]

    return catToBudget


def createBudget():
    dataToInsert = []
    listOfMethods = [lambda: chooseCategory(RegularCostCat, "CostCatName", "Set a Budget", "What budget category do you want to set?")]

    listOfMethods[0]()


def getNextID(table):

    con = sqlite3.connect("budget.db")
    cur = con.cursor()

    sqlMaxString = f"SELECT MAX({table.get_idColumnName()}) FROM {table.get_name()}"

    result = cur.execute(sqlMaxString).fetchall()

    con.close()

    if result[0][0] == None:
        return 1

    if len(result) != 1:
        print("This is an error that should never happen.")

    maxID = result[0][0]
    maxIDInt = int(maxID)
    nextID = maxIDInt + 1

    return nextID

#getNextID(SavingsCat)

def insertCategory(table, title):
    fullTitle = f"{title} Category"

    request = "What is the name of the new category?"
    printChoices(fullTitle, request, editableArea, bufferZone)

    catName = input()

    if catName == 'b':
        return catName
    
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




def createCategory():
    tables = [SavingsCat, RegularCostCat, InvestmentCat, PaymentCat, BankCat]
    choices = ["Add a Savings Category", "Add a budget category", "Add an investment category", "Add a money received category", "Add a bank category"]
    titles = ["Savings", "Budget", "Investment", "Money Received", "Bank"]

    continueChoosing = True

    while continueChoosing:
        printChoices("Create a Category", "Choose an action", editableArea, bufferZone, choices)

        userInput = getValidInt(len(choices))

        if userInput == 'b':
            continueChoosing = False

        else:
            table = tables[userInput - 1]
            title = titles[userInput - 1]

            status = insertCategory(table, title)

            if status == 'b':
                continue

            else:
                continueChoosing = False


def mainMenu():

    while True:
        choices = ["Log money in/out", "Set a budget", "Create a category"]
        printChoices("Main Menu", "Choose an Action", editableArea, bufferZone, choices)
        
        userInput = getValidInt(len(choices))

        if userInput == 1:
            moneyInOut()

        elif userInput == 2:
            createBudget()

        elif userInput == 3:
            createCategory()

        elif userInput == 'b':
            return

mainMenu()
