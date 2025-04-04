from start import *
import sqlite3

SavingsID = Column("SavingsID", "INTEGER", True, "Primary key for SavingsCat. The ID for each savings category.")
SavingsCatName = Column("SavingsCatName", "TEXT", False, "Name of Savings Category")
CreationDate = Column("CreationDate", "DATE", False, "Date category was created.")
ColumnsForSavingCat = [SavingsID, SavingsCatName, CreationDate]
SavingsCat = Table("SavingsCat", ColumnsForSavingCat, "Categories of savings.", SavingsID.get_name())

print(SavingsCat.CreateSQLTable())

allTables = [SavingsCat]

con = sqlite3.connect("budget.db")

cur = con.cursor()

for table in allTables:
    cur.execute(table.CreateSQLTable())

con.commit()

res = cur.execute(f"SELECT * FROM SavingsCat")
print(res.fetchall())

cur.execute("INSERT INTO SavingsCat (SavingsID, SavingsCatName, CreationDate) VALUES (1, \"Gas\", \"1/2/2025\")")
con.commit()

res = cur.execute(f"SELECT * FROM SavingsCat")
print(res.fetchall())