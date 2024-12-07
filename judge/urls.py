
from django.urls import path
from .views import (
    audition_list,
    performance_list,
    rate_performance,
    create_audition,
    delete_audition,
    judge_home,
    get_all_auditions,
    get_all_judges,
    get_all_performances
)

urlpatterns = [
    path('', judge_home, name='judge_home'),
    path('auditions/', audition_list, name='audition-list'),
    path('performances/', performance_list, name='performance-list'),
    path('rate/<int:audition_id>/', rate_performance, name='rate-performance'),
    path('auditions/create/', create_audition, name='create-audition'),
    path('auditions/delete/<int:audition_id>/', delete_audition, name='delete-audition'),
    path("get_all_judges/", get_all_judges),
    path("get_all_performances/", get_all_performances),
    path("get_all_auditions/", get_all_auditions)
]
