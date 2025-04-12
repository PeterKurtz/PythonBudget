from TableClasses import *

SavingsID = Column("SavingsID", "INTEGER", True, "Primary key for SavingsCat. The ID for each savings category.")
SavingsCatName = Column("SavingsCatName", "TEXT", False, "Name of Savings Category")
CreationDate = Column("CreationDate", "DATE", False, "Date category was created.")
ColumnsForSavingCat = [SavingsID, SavingsCatName, CreationDate]
SavingsCat = Table("SavingsCat", ColumnsForSavingCat, "Categories of savings.", SavingsID.get_name())

print(SavingsCat.CreateSQLTable())
print()
print(SavingsCat.createInsertString())

SavingsID = ForeignIDColumn("SavingsID", "INTEGER", False, "Savings ID for Irregular Costs", "SavingsCat", "SavingsID")
Date = Column("Date", "DATE", False, "Date when created")
Amount = Column("Amount", "INTEGER", False, "Amount for Irregular Costs")
Description = Column("Description", "TEXT", False, "Description of Costs")
ColumnsForIrregularCosts = [SavingsID, Date, Amount, Description]
IrregularCosts = Table("IrregularCosts", ColumnsForIrregularCosts, "All irregular costs used. Money that takes from savings", SavingsID.get_name())

print()

print(IrregularCosts.CreateSQLTable())
print()
print(IrregularCosts.createInsertString())