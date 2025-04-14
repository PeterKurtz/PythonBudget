from DisplayMenu import *
from userInput import *
from tableSetup import *
from datetime import date
import sqlite3

editableArea = 30
bufferZone = 3

def moneyInOut():
    print("Went to moneyInOut")

def createBudget():
    print("Went to createBudget")

def getNextID(table, idName):

    con = sqlite3.connect("budget.db")
    cur = con.cursor()
    cur = sqlite3.connect("budget.db")

    res = cur.execute(f"SELECT MAX {idName} FROM {table}")

    if len(res) != 0:
        return 1
    
    results = res.fetchall()[0]

    if len(results) != 1:
        print("This is an error that should never happen.")

    maxID = results[0]
    maxIDInt = int(maxID)
    nextID = maxIDInt + 1

    return nextID

def insertCategory(table, title):
    fullTitle = f"{title} Category"

    request = "What is the name of the new category?"
    printChoices(fullTitle, request, editableArea, bufferZone)

    catName = input()

    if catName == 'b':
        return catName
    
    else:
        insertStatement = table.createInsertStatement()
        #nextID = getNextID(table, table.get_idColumnName())

        dateCreated = date.today()


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
