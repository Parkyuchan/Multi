from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('first.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('question/', include('question.urls')),
    path('post/', include('post.urls')),
    path('product/', include('product.urls')),
]
