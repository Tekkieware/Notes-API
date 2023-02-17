from django.urls import path
from base import views


urlpatterns = [
    path('notes/', views.note_list, name='note_list'),
    path('notes/<int:pk>/', views.note_detail, name='note_detail'),
]