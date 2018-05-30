from django.urls import path
from .views import HomeView, send_contact, TestListView

app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('all/', TestListView.as_view(), name='test_vies'),
    path('send/', send_contact, name='send_contact'),
]
