from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('AppBlog.urls')),
    path('forum/', include('AppForum.urls')),
    path('accounts/', include('AppLogin.urls')),
    path('quizes/', include('AppQuiz.urls')),
]
