'''
Use bulk_create for bulk inserts and bulk_update for bulk updates.
'''

# Bulk Create
Person.objects.bulk_create([
    Person(name='John', age=30),
    Person(name='Jane', age=25),
])

# Bulk Update
persons = Person.objects.filter(age__lt=18)
for person in persons:
    person.age += 1
Person.objects.bulk_update(persons, ['age'])