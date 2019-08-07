from django.urls import path
from .views import (
    ListingDetail,
    Listings,
)
app_name = 'listings'
urlpatterns = [
    path('', Listings.as_view(), name='list'),
    path('<int:pk>/', ListingDetail.as_view(), name='detail'),
]
