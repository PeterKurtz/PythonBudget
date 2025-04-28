class Column:
    def __init__(self, name, type, isPrimary, description):
        self.name = name
        self.type = type
        self.isPrimary = isPrimary
        self.description = description

    def createSQLColumnString(self):
        sqlString = f"{self.name} {self.type}"

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

    def createForeignColumnString(self):

        sqlString = f"FOREIGN KEY({self.name}) REFERENCES {self.foreignTable}({self.foreignID})"

        return sqlString
    
class Table:
    def __init__(self, name, columnArray, description, idColumnName):
        self.name = name
        self.columnArray = columnArray
        self.description = description
        self.idColumnName = idColumnName

    def get_idColumnName(self):
        return self.idColumnName
    
    def get_name(self):
        return self.name
    
    def addCPChars(self, index, max, sqlString):
        if index != max:
            sqlString += ", "
        else:
            sqlString += ")"
        return sqlString

    def CreateSQLTable(self):

        primaryColumns = []
        foreignColumns = []

        sqlString = f"CREATE TABLE {self.name} ("
    
        for index, column in enumerate(self.columnArray):
            sqlString = f"{sqlString}\n{column.createSQLColumnString()}"
            sqlString += ", "

            if column.isPrimary:
                primaryColumns.append(column)
            if column.__class__.__name__ == "ForeignIDColumn":
                foreignColumns.append(column)
        
        sqlString += "\n"

        if len(primaryColumns) > 0:
            sqlString += "PRIMARY KEY("

            for index, pColumn in enumerate(primaryColumns):
                sqlString += pColumn.get_name()
                sqlString = self.addCPChars(index, len(primaryColumns) - 1, sqlString)

        if len(foreignColumns) > 0:
            for fColumn in foreignColumns:
                sqlString += fColumn.createForeignColumnString()

        sqlString += ")"

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
    


