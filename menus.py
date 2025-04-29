from DisplayMenu import *
from userInput import *
from tableSetup import *
from menuFunctions import *

editableArea = 40
bufferZone = 3

def moneyInOut():
    print("Went to moneyInOut")

def createBudget():
    listOfMethods = [lambda: chooseCategory(RegularCostCat, "CostCatName", "Set a Budget", "What budget category do you want to set?"),
                     lambda: printAndGetInt("Date", "What year do you want to set?", 2100),
                     lambda: printAndGetInt("Date", "What month do you want to set?", 12),
                     lambda: printAndGetFloat("Amount", "How much do you want to set?")]
    
    processData(listOfMethods, RegularCostBudget)


def createCategory():
    tables = [SavingsCat, RegularCostCat, InvestmentCat, PaymentCat, BankCat]
    choices = ["Add a Savings Category", "Add a budget category", "Add an investment category", "Add a money received category", "Add a bank category"]
    titles = ["Savings", "Budget", "Investment", "Money Received", "Bank"]

    while True:
        printChoices("Create a Category", "Choose an action", editableArea, bufferZone, choices)

        userInput = getValidInt(len(choices))

        if userInput == 'b':
            return

        else:
            table = tables[userInput - 1]
            title = titles[userInput - 1]

            status = insertCategory(table, title)

            if status == 'b':
                continue

            else:
                return

def mainMenu():

    choices = ["Log money in/out", "Set a budget", "Create a category"]
    methodsToChoose = [lambda: moneyInOut(),
                       lambda: createBudget(),
                       lambda: createCategory()]

    while True:
        printChoices("Main Menu", "Choose an Action", editableArea, bufferZone, choices)
        
        userInput = getValidInt(len(choices))

        if userInput == 'b':
            return
        
        methodsToChoose[userInput - 1]()

mainMenu()
