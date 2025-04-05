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
        
    def createInsertString(self):
        insertString = f"INSERT INTO {self.name} ("

        for index, column in enumerate(self.columnArray):
            insertString = f"{insertString}{column.get_name()}"

            if index != len(self.columnArray) - 1:
                insertString = f"{insertString}, "

            else:
                insertString = f"{insertString})"

        insertString = f"{insertString} VALUES ("

        numOfVariables = len(self.columnArray)

        for x in range(numOfVariables):
            insertString = f"{insertString}?"
            if x != numOfVariables - 1:
                insertString = f"{insertString}, "
            else:
                insertString = f"{insertString})"

        return insertString
    


