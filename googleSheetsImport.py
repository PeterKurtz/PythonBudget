from googleSheetsFunctions import *
from readingData import getCatID
from tableSetup import *
from menuFunctions import insertData, getTableChoices

creds = certify()

choices = getTableChoices(RegularCostCat, "CostCatName")

choices_array = []
choices_array.append(["Budget Categories"])

for choice in choices:
  choices_array.append([choice])

writeToSheet(creds, choices_array, "Categories!B2")

sheetValues = getSheetValues(creds, "Budget!A:E")

for index, value in enumerate(sheetValues):
  if index != 0:
    value[0] = getCatID(RegularCostCat, "CostCatName", value[0])
    insertData(RegularCosts.createInsertString(), value)

print("Successful: Delete values in first sheet.")

