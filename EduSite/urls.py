from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AppBlog.urls')),
    path('', include('AppForum.urls')),
    path('', include('AppLogin.urls')),
    path('', include('AppQuiz.urls')),
]
