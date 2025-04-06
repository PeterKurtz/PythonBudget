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
SavingsID = ForeignIDColumn("SavingsID", "INTEGER", True, "Savings ID for savings categories", "SavingsCat", "SavingsID")
GoalAmount = Column("GoalAmount", "NUMERIC", False, "Goal amount")
Date = Column("Date", "DATE", False, "Date Savings was inputed")
ColumnsForSavingsGoal = [SavingsID, GoalAmount, Date]
SavingsGoal = Table("SavingsGoal", ColumnsForSavingsGoal, "Savings Goals", "SavingsID")

#InvestmentCat Setup
InvestmentID = Column("InvestmentID", "INTEGER", True, "Investment ID")
CreationDate = Column("CreationDate", "DATE", False, "Date cateegory was created")
InvestmentName = Column("InvestmentName", "TEXT", False, "Name of category")
ColumnsForInvestmentCat = [InvestmentID, CreationDate, InvestmentName]
InvestmentCat = Table("InvestmentCat", ColumnsForInvestmentCat, "Investment Categories", "InvestmentID")

#Investments Setup
InvestmentID = ForeignIDColumn("InvestmentID", "INTEGER", True, "Investment ID for investment categories", "InvestmentCat", "InvestmentID")
Date = Column("Date", "DATE", False, "Date Investment was inputed")
AmountPaid = Column("AmountPaid", "NUMERIC", False, "Amount paid for investments")
TotalAmount = Column("TotalAmount", "NUMERIC", False, "Total amount for the category")
Description = Column("Description", "TEXT", False, "Description for the investment")
ColumnsForInvestments = [InvestmentID, Date, AmountPaid, TotalAmount, Description]
Investments = Table("Investments", ColumnsForInvestments, "Investment transactions", "InvestmentID")

#PaymentCat Setup
PaymentID = Column("PaymentID", "INTEGER", True, "Payment ID for payment categories.")
PaymentName = Column("PaymentName", "TEXT", False, "Name of Payment Category")
CreationDate = Column("CreationDate", "DATE", False, "Date category was created.")
ColumnsForPaymentCat = [PaymentID, PaymentName, CreationDate]
PaymentCat = Table("PaymentCat", ColumnsForPaymentCat, "Categories of Payments.", PaymentID.get_name())

#Payments Setup
PaymentID = ForeignIDColumn("PaymentID", "INTEGER", True, "Payment ID for payment categories", "PaymentCat", "PaymentID")
Date = Column("Date", "DATE", False, "Date Payment was inputed")
Amount = Column("Amount", "NUMERIC", False, "Amount paid")
Explanation = Column("Explanation", "TEXT", False, "Explanation for payments")
ColumnsForPayments = [PaymentID, Date, Amount, Explanation]
Payments = Table("Payments", ColumnsForPayments, "Payments", PaymentID.get_name())

#BankCat Setup
BankID = Column("BankID", "INTEGER", True, "Bank ID for bank categories.")
BankName = Column("BankName", "TEXT", False, "Name of Bank Category")
CreationDate = Column("CreationDate", "DATE", False, "Date category was created.")
ColumnsForBankCat = [BankID, BankName, CreationDate]
BankCat = Table("BankCat", ColumnsForBankCat, "Categories of Bank.", BankID.get_name())

#BankBalance Setup
BankBalanceID = ForeignIDColumn("BankBalanceID", "INTEGER", True, "Payment ID for bank categories", "BankCat", "BankBalanceID")
Date = Column("Date", "DATE", False, "Date Bank info was inputed")
BankBalance = Column("BankBalance", "NUMERIC", False, "Amount in bank.")
IsCurrent = Column("IsCurrent", "INTEGER", False, "Indicates if balance is current")
ColumnsForBankBalance = [BankBalanceID, Date, BankBalance, IsCurrent]
BankBalance = Table("BankBalance", ColumnsForBankBalance, "Bank Balance", BankBalanceID.get_name())

allTables = [RegularCosts, RegularCostCat, RegularCostBudget, SavingsCat, Savings, SavingsTotal, SavingsGoal, Savings, SavingsTotal, IrregularCosts, InvestmentCat, Payments, Investments, BankBalance, PaymentCat]
