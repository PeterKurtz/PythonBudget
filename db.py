from tableSetup import *
import sqlite3

con = sqlite3.connect("budget.db")

cur = con.cursor()

for table in allTables:
    cur.execute(table.CreateSQLTable())
    print(table.CreateSQLTable())
    print()
    print(f"Table {table.name} is set up.")
    print()

con.commit()

con.close()
