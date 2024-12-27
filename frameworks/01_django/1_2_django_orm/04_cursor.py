'''
A cursor is created by calling connection.cursor() on a django.db.connections 
object, which manages database connections. 

The cursor object is used to:

Execute SQL queries: 
    Pass a SQL query string and parameters (if needed) to cursor.execute(), and 
    the query will be executed on the database.

Fetch query results: 
    Use cursor.fetchall() or cursor.fetchone() to retrieve the 
    results of the query as a list of tuples or a single tuple, respectively.

Manipulate database state:
    Use cursor.execute() with UPDATE, INSERT, or DELETE statements to modify 
    the database.
'''

'''
Here are some key aspects of cursors in Django:

Raw SQL:
    Cursors allow you to execute raw SQL queries, bypassing Django’s ORM 
    (Object-Relational Mapping) layer. This is useful when you need to perform 
    complex queries or interact with the database in a way that’s not supported 
    by the ORM.

Parameterized queries:
    Cursors support parameterized queries, which help prevent SQL injection 
    attacks by separating user-input data from the SQL code. Use %s placeholders 
    in your query string and pass the corresponding values as a tuple to 
    cursor.execute().

Connection pooling:
    Django’s connection pooling mechanism ensures that multiple cursors can 
    share a single database connection, improving performance and reducing the 
    overhead of creating new connections.
'''

from django.db import connections

# Get a cursor object for the default database connection
cursor = connections['default'].cursor()

# Execute a raw SQL query with parameters
cursor.execute("SELECT * FROM table_name WHERE id = %s", [123])

# Fetch the query results
results = cursor.fetchall()