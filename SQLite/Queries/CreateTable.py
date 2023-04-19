import sqlite3

# Connect to a Database and create a cursor
connection = sqlite3.connect('../Databases/sqlTable.db')
cursor = connection.cursor()

# Drop the table if already exists.
cursor.execute("DROP TABLE IF EXISTS sqlTable")

# Creating table
table = """ CREATE TABLE sqlTable (
            Email VARCHAR(255) NOT NULL,
            FirstName CHAR(25) NOT NULL,
            LastName CHAR(25),
            Score INT
        ); """
cursor.execute(table)
print("Table is Ready")

# Close the connection
connection.close()
