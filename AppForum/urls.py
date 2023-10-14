from django.urls import path
from AppForum import views
app_name = 'AppForum'
urlpatterns = [
    path('ask/', views.ForumCreate, name='createforum'),
    path('', views.ForumList.as_view(), name='forumlist'),
    path('question/<pk>/', views.forumdetails, name="details"),
    path('myquestions/', views.myquestions, name='myquestions')
]