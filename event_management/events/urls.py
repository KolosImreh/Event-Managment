from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('create_event/', views.create_event, name='create_event'),
    path('update_profile/', views.update_profile, name='update_profile'),
]
