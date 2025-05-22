from django.urls import path
from . import views

urlpatterns = [
    path('teacher_choice/', views.teacher_choice, name='teacher_choice'),
]
