from TableClasses import *

#SavingsCat Setup
SavingsID = Column("SavingsID", "INTEGER", True, "Primary key for SavingsCat. The ID for each savings category.")
SavingsCatName = Column("SavingsCatName", "TEXT", False, "Name of Savings Category")
CreationDate = Column("CreationDate", "DATE", False, "Date category was created.")
ColumnsForSavingCat = [SavingsID, SavingsCatName, CreationDate]
SavingsCat = Table("SavingsCat", ColumnsForSavingCat, "Categories of savings.", SavingsID.get_name())

#IrregularCosts Setup
CostDate = Column("CostDate", "DATE", False, "Date when created")
Amount = Column("Amount", "INTEGER", False, "Amount for Irregular Costs")
Description = Column("Description", "TEXT", False, "Description of Costs")
SavingsID = ForeignIDColumn("SavingsID", "INTEGER", False, "Savings ID for Irregular Costs", "SavingsCat", "SavingsID")
ColumnsForIrregularCosts = [CostDate, Amount, Description, SavingsID]
IrregularCosts = Table("IrregularCosts", ColumnsForIrregularCosts, "All irregular costs used. Money that takes from savings", SavingsID.get_name())

#RegularCostCat Setup
CostID = Column("CostID", "INTEGER", True, "Cost ID for RegularCostCat")
CostCatName = Column("CostCatName", "TEXT", False, "Category Name")
CreationDate = Column("CreationDate", "DATE", False, "Date when created")
ColumnsForRegularCostCat = [CostID, CostCatName, CreationDate]
RegularCostCat = Table("RegularCostCat", ColumnsForRegularCostCat, "All regular cost categories", CostID.get_name())

#RegularCosts Setup
CostDate = Column("CostDate", "DATE", False, "Date cost was done")
Amount = Column("Amount", "NUMERIC", False, "Amount spent")
Explanation = Column("Explanation", "TEXT", False, "Explanation for transaction")
CostID = ForeignIDColumn("CostID", "INTEGER", False, "Cost ID for Regular Costs", "RegularCostCat", "CostID")
ColumnsForRegularCosts = [Amount, Explanation, CostDate, CostID]
RegularCosts = Table("RegularCosts", ColumnsForRegularCosts, "All regular cost transactions", CostID.get_name())

#RegularCostBudget Setup
CostYear = Column("CostYear", "INTEGER", False, "Year of budget")
CostMonth = Column("CostMonth", "INTEGER", False, "Month of budget")
Amount = Column("Amount", "NUMERIC", False, "Amount spent")
CostID = ForeignIDColumn("CostID", "INTEGER", False, "Cost ID for Regular Costs", "RegularCostCat", "CostID")
ColumnsForRegularCostBudget = [CostYear, CostMonth, Amount, CostID]
RegularCostBudget = Table("RegularCostBudget", ColumnsForRegularCostBudget, "Budget for Regular Costs", CostID.get_name())

#Savings Setup
SavingsDate = Column("SavingsDate", "DATE", False, "Date Savings was inputed")
Amount = Column("Amount", "NUMERIC", False, "Amount saved")
Explanation = Column("Explanation", "TEXT", False, "Explanation for savings")
SavingsID = ForeignIDColumn("SavingsID", "INTEGER", False, "Savings ID for savings categories", "SavingsCat", "SavingsID")
ColumnsForSavings = [SavingsDate, Amount, Explanation, SavingsID]
Savings = Table("Savings", ColumnsForSavings, "Savings", SavingsID.get_name())

#SavingsTotal Setup
SavingsDate = Column("SavingsDate", "DATE", False, "Date Savings was inputed")
Total = Column("Total", "NUMERIC", False, "Total for Savings Category")
SavingsID = ForeignIDColumn("SavingsID", "INTEGER", False, "Savings ID for savings categories", "SavingsCat", "SavingsID")
ColumnsForSavingsTotal = [SavingsDate, Total, SavingsID]
SavingsTotal = Table("SavingsTotal", ColumnsForSavingsTotal, "SavingsTotal", SavingsID.get_name())

#SavingsGoal Setup
GoalAmount = Column("GoalAmount", "NUMERIC", False, "Goal amount")
SavingsDate = Column("SavingsDate", "DATE", False, "Date Savings was inputed")
SavingsID = ForeignIDColumn("SavingsID", "INTEGER", False, "Savings ID for savings categories", "SavingsCat", "SavingsID")
ColumnsForSavingsGoal = [GoalAmount, SavingsDate, SavingsID]
SavingsGoal = Table("SavingsGoal", ColumnsForSavingsGoal, "Savings Goals", "SavingsID")

#InvestmentCat Setup
InvestmentID = Column("InvestmentID", "INTEGER", True, "Investment ID")
CreationDate = Column("CreationDate", "DATE", False, "Date cateegory was created")
InvestmentName = Column("InvestmentName", "TEXT", False, "Name of category")
ColumnsForInvestmentCat = [InvestmentID, CreationDate, InvestmentName]
InvestmentCat = Table("InvestmentCat", ColumnsForInvestmentCat, "Investment Categories", "InvestmentID")

#Investments Setup
InvestmentDate = Column("InvestmentDate", "DATE", False, "Date Investment was inputed")
AmountPaid = Column("AmountPaid", "NUMERIC", False, "Amount paid for investments")
TotalAmount = Column("TotalAmount", "NUMERIC", False, "Total amount for the category")
Description = Column("Description", "TEXT", False, "Description for the investment")
InvestmentID = ForeignIDColumn("InvestmentID", "INTEGER", False, "Investment ID for investment categories", "InvestmentCat", "InvestmentID")
ColumnsForInvestments = [InvestmentDate, AmountPaid, TotalAmount, Description, InvestmentID]
Investments = Table("Investments", ColumnsForInvestments, "Investment transactions", "InvestmentID")

#PaymentCat Setup
PaymentID = Column("PaymentID", "INTEGER", True, "Payment ID for payment categories.")
PaymentName = Column("PaymentName", "TEXT", False, "Name of Payment Category")
CreationDate = Column("CreationDate", "DATE", False, "Date category was created.")
ColumnsForPaymentCat = [PaymentID, PaymentName, CreationDate]
PaymentCat = Table("PaymentCat", ColumnsForPaymentCat, "Categories of Payments.", PaymentID.get_name())

#Payments Setup
PaymentDate = Column("PaymentDate", "DATE", False, "Date Payment was inputed")
Amount = Column("Amount", "NUMERIC", False, "Amount paid")
Explanation = Column("Explanation", "TEXT", False, "Explanation for payments")
PaymentID = ForeignIDColumn("PaymentID", "INTEGER", False, "Payment ID for payment categories", "PaymentCat", "PaymentID")
ColumnsForPayments = [PaymentDate, Amount, Explanation, PaymentID]
Payments = Table("Payments", ColumnsForPayments, "Payments", PaymentID.get_name())

#BankCat Setup
BankID = Column("BankID", "INTEGER", True, "Bank ID for bank categories.")
BankName = Column("BankName", "TEXT", False, "Name of Bank Category")
CreationDate = Column("CreationDate", "DATE", False, "Date category was created.")
ColumnsForBankCat = [BankID, BankName, CreationDate]
BankCat = Table("BankCat", ColumnsForBankCat, "Categories of Bank.", BankID.get_name())

#BankBalance Setup
BankDate = Column("BankDate", "DATE", False, "Date Bank info was inputed")
BankBalance = Column("BankBalance", "NUMERIC", False, "Amount in bank.")
IsCurrent = Column("IsCurrent", "INTEGER", False, "Indicates if balance is current")
BankBalanceID = ForeignIDColumn("BankBalanceID", "INTEGER", False, "Payment ID for bank categories", "BankCat", "BankBalanceID")
ColumnsForBankBalance = [BankDate, BankBalance, IsCurrent, BankBalanceID]
BankBalance = Table("BankBalance", ColumnsForBankBalance, "Bank Balance", BankBalanceID.get_name())

allTables = [RegularCostCat, RegularCosts, RegularCostBudget, SavingsCat, Savings, SavingsTotal, SavingsGoal, IrregularCosts, InvestmentCat, Investments, PaymentCat, Payments, BankCat, BankBalance]

for table in allTables:
    print(table.CreateSQLTable())
    print()
