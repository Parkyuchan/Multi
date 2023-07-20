from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/password/', views.change_password, name='change_password'),
]