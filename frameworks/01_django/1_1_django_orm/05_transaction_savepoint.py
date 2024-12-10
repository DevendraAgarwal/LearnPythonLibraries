'''
Transaction

transaction.atomic ensures that a block of code is executed within a 
database transaction. If any part of the block fails, the entire transaction 
is rolled back.

SavePoint

Django’s transaction management also supports savepoints, which are intermediate 
points within a transaction that can be rolled back to without rolling back the 
entire transaction.
'''

from django.db import transaction
from django.shortcuts import render
from django.http import HttpResponse
from .models import Order, Product

def create_order(request):
    try:
        with transaction.atomic():
            order = Order.objects.create(customer=request.user)
            product = Product.objects.get(id=request.POST['product_id'])
            order.items.add(product)
            order.save()
        return HttpResponse('Order created successfully')
    except Exception as e:
        return HttpResponse(f'Error: {e}')


def my_view(request):
    try:
        with transaction.atomic():
            savepoint = transaction.savepoint()
            # do_something()
            transaction.savepoint_commit(savepoint)
            # do_something_else()
    except SomeSpecificException:
        transaction.savepoint_rollback(savepoint)
    except Exception as e:
        transaction.savepoint_rollback(savepoint)
        return HttpResponse(f'Error: {e}')
