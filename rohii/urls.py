from django.urls import path
from . import views  # Ensure this is correct

urlpatterns = [
    path('', views.rohii, name='rohii'),
]
