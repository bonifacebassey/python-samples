from database.dbContext import DbContext

dbContext = DbContext()

# Drop the table if already exists.
dbContext.execute("DROP TABLE IF EXISTS SQLtable")

# Creating table
table = """ CREATE TABLE SQLtable (
            Email VARCHAR(255),
            Name VARCHAR(50),
            Score int);
        """
dbContext.execute(table)

# queries to INSERT records.
dbContext.execute('''INSERT INTO SQLtable VALUES ('bonitus@gmail.com', 'Bonitus', '100')''')
dbContext.execute('''INSERT INTO SQLtable VALUES ('pilatus@gmail.com', 'Pilatus', '82')''')
dbContext.execute('''INSERT INTO SQLtable VALUES ('quintus@gmail.com', 'Quintus', '99')''')
dbContext.execute('''INSERT INTO SQLtable VALUES ('emeritus@gmail.com', 'Emeritus', '46')''')
dbContext.execute('''INSERT INTO SQLtable VALUES ('spiritus@gmail.com', 'Spiritus', '33')''')
dbContext.execute('''INSERT INTO SQLtable VALUES ('augustus@gmail.com', 'Augustus', '27')''')

# Commit your changes in the database
dbContext.commit()

# Fetching all records
print("Fetch all records:")
dbContext.execute('''SELECT * FROM SQLtable''')
contents = dbContext.fetchall()
for content in contents:
    print(content)

# Fetching many records
print("\nFetch many records:")
dbContext.execute('''SELECT * FROM SQLtable''')
data = dbContext.fetchmany(3)
for content in contents:
    print(content)

# Fetching only one record
print("\nFetch only one record:")
dbContext.execute('''SELECT * FROM SQLtable''')
content = dbContext.fetchone()
print(content)
