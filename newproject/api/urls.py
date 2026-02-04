from django.urls import path
from api.views import get_data, create_data, user_detail

urlpatterns = [
    path('users/', get_data),
    path('users/create/', create_data),
    path('users/<int:pk>/', user_detail),
]
