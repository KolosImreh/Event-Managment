from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('events/', views.event_list, name='event_list'),  # List of events
    path('event/<int:pk>/', views.event_detail, name='event_detail'),  # Event detail (requires event ID)
    path('create_event/', views.create_event, name='create_event'),  # Create event
    path('update_profile/', views.update_profile, name='update_profile'),  # Update profile
]
