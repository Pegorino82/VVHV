from django.urls import path
from personsapp.views import PersonCreateView, PersonListView, PersonDetailView

app_name = 'personsapp'

urlpatterns = [
    path('', PersonListView.as_view(), name='list_view'),
    path('create', PersonCreateView.as_view(), name='create_view'),
    path('detail/<int:pk>', PersonDetailView.as_view(), name='detail_view'),
]
