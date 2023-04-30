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

print("Display table details in ascending order based on Address:")
query_ascending = "SELECT * from Customers ORDER BY Address ASC"
cursor = dbContext.execute(query_ascending)
for c in cursor:
    print(c)


print("\nDisplay Address and Id based on the address in descending order:")
query_descending = "SELECT Address, Id from Customers ORDER BY Address DESC"
cursor = dbContext.execute(query_descending)
for c in cursor:
    print(c)


print("\nDisplay Name and Id based on Name in descending order:")
query_descending = "SELECT Name, Id from Customers ORDER BY Name DESC"
cursor = dbContext.execute(query_descending)
for c in cursor:
    print(c)
