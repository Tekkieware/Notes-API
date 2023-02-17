from django.urls import path
import views


urlpatterns = [
    path('notes/', views.note_list, 'note_list'),
    path('notes/<int:pk>/', views.note_detail, 'note_detail'),
]