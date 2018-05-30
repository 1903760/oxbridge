from django.urls import path
from .views import OrderView
from django.views.generic.base import TemplateView

app_name = 'orders'
urlpatterns = [
    path('demo/', TemplateView.as_view(template_name='orders/demo.html'), name='demo'),
    path('give/<slug:slug>/', OrderView.as_view(), name='test'),
]
