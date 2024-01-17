from django.urls import path

from .views import profile_create_page, profile_update_page

urlpatterns = [
    path('create/', profile_create_page, name='create_profile'),
    path('update/<int:pk>/', profile_update_page, name='update_profile'),
]