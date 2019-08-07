from django.urls import path
from .views import (
    login_page,
    logout_page,
    dashboard,
    register_page
)

app_name = 'accounts'
urlpatterns = [
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('logout/', logout_page, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
]
