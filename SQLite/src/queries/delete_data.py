from dbContext import DbContext

dbContext = DbContext()

# Drop the table if already exists.
dbContext.execute("DROP TABLE IF EXISTS YOCTO")

# Creating table
table = """ CREATE TABLE YOCTO (
            Email VARCHAR(255) NOT NULL,
            Name CHAR(25) NOT NULL,
            Score INT);
        """
dbContext.execute(table)

# queries to INSERT records.
dbContext.execute('''INSERT INTO YOCTO VALUES ('bonitus@gmail.com', 'Bonitus', '25')''')
dbContext.execute('''INSERT INTO YOCTO VALUES ('pilatus@gmail.com', 'Pilatus', '15')''')
dbContext.execute('''INSERT INTO YOCTO VALUES ('quintus@gmail.com', 'Quintus', '36')''')
dbContext.execute('''INSERT INTO YOCTO VALUES ('emeritus@gmail.com', 'Emeritus', '27')''')
dbContext.execute('''INSERT INTO YOCTO VALUES ('spiritus@gmail.com', 'Spiritus', '40')''')
dbContext.execute('''INSERT INTO YOCTO VALUES ('augustus@gmail.com', 'Augustus', '14')''')
dbContext.execute('''INSERT INTO YOCTO VALUES ('yoctopoky@gmail.com', 'YoctoPoky', '10')''')

dbContext.execute("SELECT * FROM YOCTO")
print(dbContext.fetchall())

print("\nDELETE all with Score < 15")
dbContext.execute("DELETE FROM YOCTO WHERE Score < 15")
dbContext.execute("SELECT * FROM YOCTO")
print(dbContext.fetchall())

dbContext.execute("DELETE FROM YOCTO")
print("\nAfter DELETING all rows")
dbContext.execute("SELECT * FROM YOCTO")
print(dbContext.fetchall())

# Commit your changes
dbContext.commit()
