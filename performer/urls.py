
from django.urls import path
from . import views

urlpatterns = [
    path('auditions/', views.auditions_list, name='auditions-list'),
    path('auditions/join/<int:audition_id>/', views.join_audition, name='join-audition'),
    path('', views.performer_home, name='performer_home'),  # Existing
    path("get_all_performers/", views.get_all_performers)
]

