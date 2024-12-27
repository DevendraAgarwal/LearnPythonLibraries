# Django CRUD REST API

Creating a CRUD API using Django involves setting up Django with Django REST Framework (DRF). Here's a step-by-step guide to creating a basic CRUD API.

## Step 1: Set Up the Project

Install Django and Django REST Framework:

```bash
Copy code
pip install django djangorestframework

```

Create a new Django project:

```bash
Copy code
django-admin startproject myproject
cd myproject

```

Create a new app:

```bash
Copy code
python manage.py startapp myapp

```

Add rest_framework and your new app to INSTALLED_APPS in myproject/settings.py:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'myapp',
]

```

## Step 2: Create the Model

In myapp/models.py, define a simple model:

```python
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

```

## Step 3: Create the Serializer

In myapp/serializers.py, create a serializer for the model:

```python
from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

```

## Step 4: Create the Views

In myapp/views.py, create the views using Django REST Framework's viewsets:

```python
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

```

## Step 5: Set Up the URLs

In myapp/urls.py, set up the URLs for the API:

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

```

Include the app's URLs in the project's urls.py:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),
]

```

## Step 6: Run Migrations

Run the following commands to create the database tables:

```bash
python manage.py makemigrations
python manage.py migrate

```

## Step 7: Run the Server

Finally, run the development server:

```bash
python manage.py runserver

```

## Step 8: Test the API

You can now test the CRUD API using a tool like Postman or curl. The endpoints are:

```
GET /api/items/ - List all items
POST /api/items/ - Create a new item
GET /api/items/<id>/ - Retrieve a specific item
PUT /api/items/<id>/ - Update a specific item
DELETE /api/items/<id>/ - Delete a specific item

```

## Additional Steps

For a more complete and secure application, consider adding:

- Authentication and permissions.
- Validation.
- Error handling.
- Pagination.

This basic setup should get you started with a CRUD API using Django and Django REST Framework
