"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path  # Ensure this is imported
from django.conf import settings
from django.conf.urls.static import static
from blog.views import post_list, post_detail, post_new, edit_post, delete_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', post_list, name='post_list'),
    path('blog/new/', post_new, name='post_new'),
    path('blog/<int:post_id>/', post_detail, name='post_detail'),
    path('blog/<int:post_id>/edit/', edit_post, name='edit_post'),
    path('blog/<int:post_id>/delete/', delete_post, name='delete_post'),
]

# Static and media files in development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)