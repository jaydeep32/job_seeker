from django.urls import path
from job import views

app_name = 'job'


urlpatterns = [
    path('', views.index, name='home'),
    path('post/listing/', views.post_listing, name='post-listing-all'),
    path('post/listing/<str:slug>/', views.post_listing, name='post-listing'),
    path('post/detail/<str:slug>/', views.post_detail, name='post-detail'),

    path('post/job-add/', views.add_job, name='add-job'),
    path('post/job-add/<str:slug>/', views.add_job, name='update-job'),
    path('company-add/', views.add_company, name='add-company'),
    path('company-add/<int:pk>/', views.add_company, name='update-company'),
    path('company-detail/', views.company_detail, name='company-detail'),
]
