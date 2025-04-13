from DisplayMenu import *
from userInput import *

editableArea = 30
bufferZone = 3

def moneyInOut():
    print("Went to moneyInOut")

def createBudget():
    print("Went to createBudget")

def createCategory():
    print("Went to createCategory")

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
