'''
select_related() "follows" foreign-key relationships, selecting additional 
    related-object data when it executes its query.

prefetch_related() does a separate lookup for each relationship, and does the 
    "joining" in Python.
'''

# Select Related
'''
Purpose:
    To create a single SQL query with JOINs to fetch related objects, 
    thereby reducing the number of database hits.

Use Case:
    Suitable for foreign keys and one-to-one fields.

How It Works:
    Fetches the related objects in the same query as the main object using SQL joins.

'''

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

class Author(models.Model):
    name = models.CharField(max_length=100)
    books = Book.objects.select_related('author')

for book in books:
    print(book.author.name)


# PreFetch Related
'''
Purpose:
    To create additional separate SQL queries and perform the fetching of related 
    objects in a second query, optimizing the retrieval of many-to-many and 
    reverse foreign key relationships.

Use Case:
    Suitable for many-to-many fields and reverse foreign key relationships.

How It Works:
    Fetches the related objects in separate queries and does the joining in Python.

'''

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')

class Author(models.Model):
    name = models.CharField(max_length=100)
    books = Book.objects.prefetch_related('authors')

for book in books:
    print([author.name for author in book.authors.all()])
