from django.urls import path

from .views import (add_job_page, add_job_success,
                    all_jobs, job_detail, job_region)

urlpatterns = [
    path('add-job/', add_job_page, name='add_job_page'),
    path('success/', add_job_success, name='add_job_success'),
    path('all/', all_jobs, name='all_jobs'),
    path('detail/<int:pk>/', job_detail, name='job_detail'),
    path('region/<int:pk>/', job_region, name='job_region'),
]