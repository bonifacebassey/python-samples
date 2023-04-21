import sqlite3

# Connect to a Database and create a cursor
connection = sqlite3.connect("../Databases/sqlFetchFromTable.db")
cursor = connection.cursor()

# Drop the table if already exists.
cursor.execute("DROP TABLE IF EXISTS Fetch4rmTable")

# Creating table
table = """ CREATE TABLE Fetch4rmTable (
            Email VARCHAR(255),
            Name VARCHAR(50),
            Score int);
        """
cursor.execute(table)

# Queries to INSERT records.
cursor.execute('''INSERT INTO Fetch4rmTable VALUES ('bonitus@gmail.com', 'Bonitus', '100')''')
cursor.execute('''INSERT INTO Fetch4rmTable VALUES ('pilatus@gmail.com', 'Pilatus', '82')''')
cursor.execute('''INSERT INTO Fetch4rmTable VALUES ('quintus@gmail.com', 'Quintus', '99')''')
cursor.execute('''INSERT INTO Fetch4rmTable VALUES ('emeritus@gmail.com', 'Emeritus', '46')''')
cursor.execute('''INSERT INTO Fetch4rmTable VALUES ('spiritus@gmail.com', 'Spiritus', '33')''')
cursor.execute('''INSERT INTO Fetch4rmTable VALUES ('augustus@gmail.com', 'Augustus', '27')''')

# Commit your changes in the database
connection.commit()

# Fetching all records
print("Fetch all records:")
cursor.execute('''SELECT * FROM Fetch4rmTable''')
data = cursor.fetchall()
for row in data:
    print(row)

# Fetching many records
print("\nFetch many records:")
cursor.execute('''SELECT * FROM Fetch4rmTable''')
data = cursor.fetchmany(3)
for row in data:
    print(row)

# Fetching only one record
print("\nFetch only one record:")
cursor.execute('''SELECT * FROM Fetch4rmTable''')
data = cursor.fetchone()
print(data)
