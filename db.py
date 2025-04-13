from tableSetup import *
import sqlite3

con = sqlite3.connect("budget.db")

cur = con.cursor()

for table in allTables:
    print(f"Table {table.name} is set up.")
    cur.execute(table.CreateSQLTable())

con.commit()

con.close()
