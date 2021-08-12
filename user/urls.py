from django.urls import path
from user import views
from django.contrib.auth.views import LogoutView


app_name = 'user'

urlpatterns = [
    path('login/', views.CustomeLogin.as_view(), name='login'),
    path('register/', views.custome_register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]


