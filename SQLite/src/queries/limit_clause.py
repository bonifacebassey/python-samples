from dbContext import DbContext

dbContext = DbContext()

# Drop the table if already exists.
dbContext.execute("DROP TABLE IF EXISTS Customers")

# Creating table
table = """ CREATE TABLE Customers (
            Id INT PRIMARY KEY NOT NULL,
            Name TEXT NOT NULL,
            Age INT NOT NULL,
            Address CHAR(50));
        """
dbContext.execute(table)

# queries to INSERT records.
dbContext.execute('''INSERT INTO Customers VALUES (1, 'Bonitus', '22', 'Abuja')''')
dbContext.execute('''INSERT INTO Customers VALUES (2, 'Pilatus', '82', 'Freiburg')''')
dbContext.execute('''INSERT INTO Customers VALUES (3, 'Emeritus', '46', 'Lagos')''')
dbContext.execute('''INSERT INTO Customers VALUES (4, 'Spiritus', '33', 'Denmark')''')
dbContext.execute('''INSERT INTO Customers VALUES (5, 'Augustus', '27', 'Cuba')''')

# Commit your changes
dbContext.commit()

print("\nLIMIT keyword is used to limit the data given by the SELECT statement:")
query_ascending = "SELECT * from Customers LIMIT 3"
cursor = dbContext.execute(query_ascending)
for c in cursor:
    print(c)
