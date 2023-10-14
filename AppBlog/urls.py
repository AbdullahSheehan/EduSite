from django.urls import path
from AppBlog import views
app_name = 'AppBlog'
urlpatterns = [
    path('create/', views.createArticle, name="createblog"),
    path('', views.ArticleList.as_view(), name='articles'),
    path('<slug>/', views.ArticleDetail.as_view(), name='articledetails')
]