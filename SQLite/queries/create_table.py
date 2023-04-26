from database.dbContext import DbContext

dbContext = DbContext()

# Drop the table if already exists.
dbContext.execute("DROP TABLE IF EXISTS SQLtable")

# Creating table
table = """ CREATE TABLE SQLtable (
            Email VARCHAR(255) NOT NULL,
            FirstName CHAR(25) NOT NULL,
            LastName CHAR(25),
            Score INT );
        """
dbContext.execute(table)
print("SQL table is created")
