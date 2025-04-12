from tableSetup import *
import sqlite3

con = sqlite3.connect("budget.db")

cur = con.cursor()

for table in allTables:
    print(table.name)
    cur.execute(table.CreateSQLTable())

con.commit()

res = cur.execute(f"SELECT * FROM SavingsCat")
print(res.fetchall())

cur.execute("INSERT INTO SavingsCat (SavingsID, SavingsCatName, CreationDate) VALUES (1, \"Gas\", \"1/2/2025\")")
con.commit()

res = cur.execute(f"SELECT * FROM SavingsCat")
print(res.fetchall())