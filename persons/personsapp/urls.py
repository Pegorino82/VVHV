from django.urls import path
from personsapp.views import PersonListView, PersonCreateView

app_name = 'personsapp'

urlpatterns = [
    path('', PersonListView.as_view(), name='list_view'),
    path('/create', PersonCreateView.as_view(), name='create_view'),
]
