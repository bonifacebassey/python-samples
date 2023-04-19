import sqlite3

connection = None
try:
    # Connect to a DB and create a cursor
    connection = sqlite3.connect("sql.db")
    cursor = connection.cursor()
    print('sql.db Init')

    # Write a query and execute it with cursor
    query = "SELECT sqlite_version()"
    cursor.execute(query)

    # Fetch and output result
    result = cursor.fetchall()
    print('SQLite Version is {}'.format(result))

    # Close the cursor
    cursor.close()

# Handle errors
except sqlite3.Error as error:
    print('Error occurred - ', error)

finally:
    if connection:
        connection.close()
        print('SQLite Connection closed')
