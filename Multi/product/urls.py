from django.urls import path
from . import views

urlpatterns = [
    path('center/', views.center, name='center'),
    path('list/', views.ProductList.as_view()),
    path('category/<str:slug>/', views.category_page),
]