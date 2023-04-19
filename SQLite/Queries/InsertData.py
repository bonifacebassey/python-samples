import sqlite3

# Connect to a Database and create a cursor
connection = sqlite3.connect('../Databases/sqlInsertData.db')
cursor = connection.cursor()

# Drop the table if already exists.
cursor.execute("DROP TABLE IF EXISTS STUDENT")

# Creating table
table = """ CREATE TABLE STUDENT (
            Name VARCHAR(255),
            Class VARCHAR(255),
            Section VARCHAR(255));
        """
cursor.execute(table)

# Queries to INSERT records.
cursor.execute('''INSERT INTO STUDENT VALUES ('Bonitus', '7th', 'A')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Pilatus', '8th', 'B')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Quintus', '9th', 'C')''')

# Display data inserted
print("Showing the table content:")
data = cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)

# Commit your changes in the database
connection.commit()

# Closing the connection
connection.close()
