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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog.views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', PostList.as_view(), name='post_list'),  # Use CBV with as_view()
    path('blog/new/', PostCreate.as_view(), name='post_create'),  # Use CBV for new post
    path('blog/<int:pk>/', PostDetail.as_view(), name='post_detail'),  # CBV for detail
    path('blog/<int:pk>/edit/', PostUpdate.as_view(), name='edit_post'),  # CBV for edit
    path('blog/<int:pk>/delete/', PostDelete.as_view(), name='delete_post'),  # CBV for delete
]

# Static and media files in development
if settings.DEBUG:  # Ensure these are only for development
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
