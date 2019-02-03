from django.urls import path
from personsapp.views import list_view

app_name = 'personsapp'

urlpatterns = [
    path('', list_view, name='list_view'),
]