from django.urls import path
from . import views
urlpatterns = [
    # 게시물 수정하는 페이지 url연결
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('create_post/', views.createPost),
    path('<int:pk>/update_post/', views.postUpdate),
    path('<int:pk>/delete_post/', views.delete_post),
    path('<str:q>/search/', views.PostSearch.as_view()),
]