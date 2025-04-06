from start import *

#SavingsCat Setup
SavingsID = Column("SavingsID", "INTEGER", True, "Primary key for SavingsCat. The ID for each savings category.")
SavingsCatName = Column("SavingsCatName", "TEXT", False, "Name of Savings Category")
CreationDate = Column("CreationDate", "DATE", False, "Date category was created.")
ColumnsForSavingCat = [SavingsID, SavingsCatName, CreationDate]
SavingsCat = Table("SavingsCat", ColumnsForSavingCat, "Categories of savings.", SavingsID.get_name())

#IrregularCosts Setup
SavingsID = ForeignIDColumn("SavingsID", "INTEGER", True, "Savings ID for Irregular Costs", "SavingsCat", "SavingsID")
Date = Column("Date", "DATE", False, "Date when created")
Amount = Column("Amount", "INTEGER", False, "Amount for Irregular Costs")
Description = Column("Description", "TEXT", False, "Description of Costs")
ColumnsForIrregularCosts = [SavingsID, Date, Amount, Description]
IrregularCosts = Table("IrregularCosts", ColumnsForIrregularCosts, "All irregular costs used. Money that takes from savings", SavingsID.get_name())

#RegularCostCat Setup
CostID = Column("CostID", "INTEGER", True, "Cost ID for RegularCostCat")
CostCatName = Column("CostCatName", "TEXT", False, "Category Name")
CreationDate = Column("CreationDate", "DATE", False, "Date when created")
ColumnsForRegularCostCat = [CostID, CostCatName, CreationDate]
RegularCostCat = Table("RegularCostCat", ColumnsForRegularCostCat, "All regular cost categories", CostID.get_name())

#RegularCosts Setup
CostID = ForeignIDColumn("CostID", "INTEGER", True, "Cost ID for Regular Costs", "RegularCostCat", "CostID")
Date = Column("Date", "DATE", False, "Date cost was done")
Amount = Column("Amount", "NUMERIC", False, "Amount spent")
Explanation = Column("Explanation", "TEXT", False, "Explanation for transaction")
ColumnsForRegularCosts = [CostID, Date, Amount, Explanation]
RegularCosts = Table("RegularCosts", ColumnsForRegularCosts, "All regular cost transactions", CostID.get_name())

#RegularCostBudget Setup
CostID = ForeignIDColumn("CostID", "INTEGER", True, "Cost ID for Regular Costs", "RegularCostCat", "CostID")
Date = Column("Date", "DATE", False, "Date cost was done")
Amount = Column("Amount", "NUMERIC", False, "Amount spent")
ColumnsForRegularCostBudget = [CostID, Date, Amount]
RegularCostBudget = Table("RegularCostBudget", ColumnsForRegularCostBudget, "Budget for Regular Costs", CostID.get_name())

#Savings Setup
SavingsID = ForeignIDColumn("SavingsID", "INTEGER", True, "Savings ID for savings categories", "SavingsCat", "SavingsID")
Date = Column("Date", "DATE", False, "Date Savings was inputed")
Amount = Column("Amount", "NUMERIC", False, "Amount saved")
Explanation = Column("Explanation", "TEXT", False, "Explanation for savings")
ColumnsForSavings = [SavingsID, Date, Amount, Explanation]
Savings = Table("Savings", ColumnsForSavings, "Savings", SavingsID.get_name())

#SavingsTotal Setup
SavingsID = ForeignIDColumn("SavingsID", "INTEGER", True, "Savings ID for savings categories", "SavingsCat", "SavingsID")
Date = Column("Date", "DATE", False, "Date Savings was inputed")
Total = Column("Total", "NUMERIC", False, "Total for Savings Category")
ColumnsForSavingsTotal = [SavingsID, Date, Total]
SavingsTotal = Table("SavingsTotal", ColumnsForSavingsTotal, "SavingsTotal", SavingsID.get_name())

#SavingsGoal Setup
