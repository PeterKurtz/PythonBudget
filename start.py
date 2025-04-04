class Column:
    def __init__(self, name, type, isPrimary, description):
        self.name = name
        self.type = type
        self.isPrimary = isPrimary
        self.description = description

    def createSQLColumnString(self):
        sqlString = f"{self.name} {self.type}"
        
        if self.isPrimary:
            sqlString = f"{sqlString} PRIMARY KEY"

        return sqlString
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
class ForeignIDColumn(Column):
    def __init__(self, name, type, isPrimary, description, foreignTable, foreignID):
        super().__init__(name, type, isPrimary, description)

        self.foreignTable = foreignTable
        self.foreignID = foreignID

    def createSQLColumnString(self):

        sqlString = f"FOREIGN KEY({self.name}) References {self.foreignTable} ({self.foreignID})"

        return sqlString
    
class Table:
    def __init__(self, name, columnArray, description, idColumnName):
        self.name = name
        self.columnArray = columnArray
        self.description = description
        self.idColumnName = idColumnName

    def CreateSQLTable(self):

        sqlString = f"CREATE TABLE {self.name} ("
    
        for index, column in enumerate(self.columnArray):
            sqlString = f"{sqlString}\n{column.createSQLColumnString()}"
            if index != len(self.columnArray) - 1:
                sqlString = f"{sqlString},"

            else:
                sqlString = f"{sqlString})"

        return sqlString
        
    def createInsertString(self, numOfValues):
        insertString = f"INSERT INTO {self.name} ("

        for index, column in enumerate(len(self.columnArray)):
            insertString = f"{insertString},"

            if index != len(self.columnArray) - 1:
                insertString = f"{insertString}"

            else:
                insertString = f"{insertString})"

            insertString = f"{insertString} VALUES ("

        for x in range(numOfValues):
            insertString = f"{insertString} ?"
            if x != len(numOfValues) - 1:
                insertString = f"{insertString}, "

            else:
                insertString = f"{insertString})"

        return insertString
    
SavingsID = Column("SavingsID", "INTEGER", True, "Primary key for SavingsCat. The ID for each savings category.")
SavingsCatName = Column("SavingsCatName", "TEXT", False, "Name of Savings Category")
CreationDate = Column("CreationDate", "DATE", False, "Date category was created.")
ColumnsForSavingCat = [SavingsID, SavingsCatName, CreationDate]
SavingsCat = Table("SavingsCat", ColumnsForSavingCat, "Categories of savings.", SavingsID.get_name())

print(SavingsCat.CreateSQLTable())
