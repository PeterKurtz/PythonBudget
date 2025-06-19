from DisplayMenu import *
from userInput import *
from tableSetup import *
from menuFunctions import *

def moneyInOut():
    title = "Log Money In/Out"
    request = "Select an action"
    choices = ["Add money spent on the budget", "Add money spent on savings", "Add money saved", "Add money invested", "Add money received", "Update total in bank"]

    printMenu(title, request, choices)

    listOfMethods = [lambda: moneySpentOnBudget(), 
                     lambda: moneySpentOnSavings(), 
                     lambda: addMoneySaved(), 
                     lambda: addMoneyInvested(),
                     lambda: addMoneyReceived(), 
                     lambda: updateBank()]
    
    while True:
        userInput = getValidInt(len(choices))

        if userInput == 'b':
            return

        methodStatus = listOfMethods[userInput - 1]()

        if methodStatus == 'b':
            continue

        else:
            return

def createBudget():
    title = "Set a Budget"
    listOfMethods = [lambda: chooseCategory(RegularCostCat, "CostCatName", title, "What budget category do you want to set?"),
                     lambda: printAndGetInt(title, "What year do you want to set?", 2100),
                     lambda: printAndGetInt(title, "What month do you want to set?", 12),
                     lambda: printAndGetFloat("Amount", "How much do you want to set?")]
    
    processData(listOfMethods, RegularCostBudget)

def createCategory():
    tables = [SavingsCat, RegularCostCat, InvestmentCat, PaymentCat, BankCat]
    choices = ["Add a Savings Category", "Add a budget category", "Add an investment category", "Add a money received category", "Add a bank category"]
    titles = ["Savings", "Budget", "Investment", "Money Received", "Bank"]

    while True:
        printMenu("Create a Category", "Choose an action", choices)

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
            
def setGoal():
    title = "Set a Savings Goal"
    listOfMethods = [lambda: chooseCategory(SavingsCat, "SavingsCatName", title, "What savings category do you want to set?"),
                     lambda: printAndGetFloat("Amount", "How much do you want to set?"),
                     lambda: printAndGetDate(title, "What date do you want the goal to be set for?")
                    ]
    
    processData(listOfMethods, SavingsGoal)

def mainMenu():

    choices = ["Log money in/out", "Set a budget", "Create a category", "Set a savings goal"]
    methodsToChoose = [lambda: moneyInOut(),
                       lambda: createBudget(),
                       lambda: createCategory(),
                       lambda: setGoal()]

    while True:
        printMenu("Main Menu", "Choose an Action", choices)
        
        userInput = getValidInt(len(choices))

        if userInput == 'b':
            return
        
        methodsToChoose[userInput - 1]()

mainMenu()
