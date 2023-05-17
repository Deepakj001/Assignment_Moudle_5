from django.urls import path, include
from .views import *

urlpatterns = [
    path('',index, name= 'index'),
    path('add_product/',add_product, name='add_product'),
    path('edit_product/<int:pid>',edit_product,name='edit_products'),
]