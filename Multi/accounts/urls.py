from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/password/', views.change_password, name='change_password'),
    path('delete/', views.delete, name='delete'),
    path('<int:pk>/choice_volunteer/', views.volunteer_choice, name='volunteer_choice'),
    path('<int:pk>/choice_alone/', views.alone_choice, name='alone_choice'),
]