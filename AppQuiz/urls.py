from django.urls import path
from AppQuiz import views
app_name = 'AppQuiz'
urlpatterns = [
    path('',views.AllQuiz.as_view(), name='quizhome'),
    path('myquiz/', views.MyQuiz, name='myquizes'),
    path('createquiz/', views.create_quiz, name='createquiz'),
    path('<pk>/', views.quiz_details, name='quizdetails'),
    path('customize/<pk>/', views.customize_quiz, name='customizequiz'),
    path('exam/<pk>/', views.givequiz, name='inquiz'),
    path('result/<pk>/', views.quizresult, name='quizresult'),
]