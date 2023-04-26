from database.dbContext import DbContext

dbContext = DbContext()

# Write a query and execute it with cursor
query = "SELECT sqlite_version()"
dbContext.execute(query)

# Fetch and output result
result = dbContext.fetchall()
print('SQLite Version is {}'.format(result))
