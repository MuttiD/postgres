import psycopg2


# connect to chinook database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records  from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the Name column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only Queen column from the "Artist" table
cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the results (single)
# results = cursor.fecthone()

# close the connection
connection.close()

# print the results
for result in results:
    print(result)