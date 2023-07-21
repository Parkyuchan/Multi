from django.urls import path
from . import views

urlpatterns = [
    path('', views.QuestionList.as_view()),
    path('<int:pk>/', views.QuestionDetail.as_view()),
    path('<int:pk>/complete/', views.complete, name='complete'),
]