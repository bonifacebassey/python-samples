from dbContext import DbContext

# JOIN clause combines the record from two tables in the basis of common attributes
# INNER JOIN (JOIN):    Gives records that have common attributes in both tables
# LEFT JOIN:            Gives all records from the left and only the common record from the right
# RIGHT JOIN:           Gives all records from the right and only the common record from the left
# FULL OUTER JOIN:      Gives all records when there is a common attribute in either left or right table
# CROSS JOIN:           Gives records of one table with all other records of another table

dbContext = DbContext()

# Drop the table if already exists.
dbContext.execute("DROP TABLE IF EXISTS Advisor")
dbContext.execute("DROP TABLE IF EXISTS Student")

# Creating table
tables = '''CREATE TABLE Advisor(
                AdvisorId INTEGER NOT NULL,
                AdvisorName TEXT NOT NULL,
                PRIMARY KEY(AdvisorId)
            );
                
            CREATE TABLE Student(
                StudentId NUMERIC NOT NULL,
                StudentName NUMERIC NOT NULL,
                AdvisorId INTEGER,
                FOREIGN KEY(AdvisorId) REFERENCES Advisor(AdvisorId),
                PRIMARY KEY(StudentId)
            );
                
            INSERT INTO Advisor(AdvisorId, AdvisorName) VALUES
                (1, "Regina Ekpenyong"), 
                (2, "Ngozi Adichie"), 
                (3, "Nathaniel Bassey"),
                (4, "Peter Obi"),
                (5, "King Arthur");
                
            INSERT INTO Student(StudentId, StudentName, AdvisorId) VALUES
                (501, "Yocto", 1),
                (502, "Yocto", 1),
                (503, "Yocto", 3),
                (504, "Yocto", 2),
                (505, "Yocto", 4),
                (506, "Yocto", 2),
                (507, "Yocto", 2),
                (508, "Yocto", 3),
                (509, "Yocto", NULL),
                (510, "Yocto", 1);
        '''
dbContext.executescript(tables)

# Commit your changes
dbContext.commit()

# INNER JOIN Syntax:
'''SELECT columns
   FROM table1
   [INNER] JOIN table2
   ON table1.column = table2.column;
'''
print("\nINNER JOIN Syntax:")
query_inner_join = '''
                    SELECT StudentId, StudentName, AdvisorName
                    FROM Student
                    INNER JOIN Advisor
                    ON Student.AdvisorId == Advisor.AdvisorId
                   '''
dbContext.execute(query_inner_join)
result = dbContext.fetchall()
for r in result:
    print(r)


# LEFT JOIN Syntax:
'''SELECT columns
   FROM table1
   LEFT JOIN table2
   ON table1.column = table2.column;
'''
print("\nLEFT JOIN Syntax:")
query_left_join = '''
                    SELECT StudentId, StudentName, AdvisorName
                    FROM Student
                    LEFT JOIN Advisor
                    ON Student.AdvisorId == Advisor.AdvisorId
                   '''
dbContext.execute(query_left_join)
result = dbContext.fetchall()
for r in result:
    print(r)


print("\nRIGHT and FULL OUTER JOINs are not currently supported")

# CROSS JOIN Syntax:
'''SELECT columns
   FROM table1
   CROSS JOIN table2;
'''
print("\nCROSS JOIN Syntax:")
cross_join = '''
                SELECT StudentId, StudentName, AdvisorName
                FROM Student
                LEFT JOIN Advisor
            '''
dbContext.execute(cross_join)
result = dbContext.fetchall()
for r in result:
    print(r)


