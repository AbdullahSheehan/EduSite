from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('AppBlog.urls')),
    path('forum/', include('AppForum.urls')),
    path('accounts/', include('AppLogin.urls')),
    path('quizes/', include('AppQuiz.urls')),
]

from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)