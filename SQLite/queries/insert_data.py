from database.dbContext import DbContext

dbContext = DbContext()

# Drop the table if already exists.
dbContext.execute("DROP TABLE IF EXISTS SQLtable")

# Creating table
table = """ CREATE TABLE SQLtable (
            Name VARCHAR(255),
            Class VARCHAR(255),
            Section VARCHAR(255));
        """
dbContext.execute(table)

# queries to INSERT records.
dbContext.execute('''INSERT INTO SQLtable VALUES ('Bonitus', '7th', 'A')''')
dbContext.execute('''INSERT INTO SQLtable VALUES ('Pilatus', '8th', 'B')''')
dbContext.execute('''INSERT INTO SQLtable VALUES ('Quintus', '9th', 'C')''')

# Display data inserted
print("Showing the table content:")
contents = dbContext.execute('''SELECT * FROM SQLtable''')
for content in contents:
    print(content)

# Commit your changes in the database
dbContext.commit()
