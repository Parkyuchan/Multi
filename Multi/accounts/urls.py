from django.urls import path
from . import views
app_name = 'accounts'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/password/', views.change_password, name='change_password'),
    path('delete/', views.delete, name='delete'),
    path('<int:pk>/profile/', views.profile, name='profile'),
    path('<int:pk>/follow/', views.follow, name='follow'),
    path('<int:pk>/profile_register', views.profile_register, name='profile_register'),
]