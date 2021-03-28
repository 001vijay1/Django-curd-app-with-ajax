from django.urls import path
from .views import index,Add_data,delete_data,edit_data

urlpatterns = [
    path('', index, name='index'),
    path('delete_data/', delete_data, name='delete_data'),
    path('Add_data', Add_data, name='Add_data'),
    path('edit_data/', edit_data, name='edit_data'),
]
