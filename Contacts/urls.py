from django.urls import path
from .views import inquiry_page

app_name = 'Contacts'
urlpatterns = [
    path('inquiry/', inquiry_page, name='inquiry'),
]
