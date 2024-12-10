from django.db import models
import uuid

class BaseModel(models.Model):
    '''
    This Base Model will now use as a Parent or Base Class for other Models
    Those model will auto generate uid and created_at field
    There will be no Table and Model Will Create in Database
    '''
    uid = models.UUIDField(default=uuid.uuid4,
                        primary_key=True,
                        editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True

'''
on_delete=models.CASCADE  -> For Cascading Delete
on_delete=models.SET_NULL -> It Will Set Null If Parent Record Deleted
on_delete=models.SET_DEFAULT -> It Will Set Default Value If Parent Record Deleted
'''

'''
Queries:

ModelName.objects.function(args)

Example:

People.objects.get(24) -> QuerySet of People Object Where Primary Id is 24
People.objects.exclude(age<18) -> QuerySet of People Object Except where age is less than 24
People.objects.filter(age=18) -> QuerySet of People Object where age is 24
People.objects.all() -> QuerySet of All People Object 
'''