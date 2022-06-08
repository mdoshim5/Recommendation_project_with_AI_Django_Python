from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.profile_view, name='profile'),    
    path('edit', views.edit_profile, name='edit_profile'),    
]