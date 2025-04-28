import sqlite3

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

def getCatID(table, catName):
    con = sqlite3.connect("budget.db")
    cur = con.cursor()

    sqlString = f"SELECT {table.get_idColumnName()} FROM {table.get_name()} WHERE CostCatName = \"{catName}\""

    result = cur.execute(sqlString).fetchall()

    id = result[0][0]

    idInt = int(id)

    return idInt

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

