from django.urls import path
from AppLogin import views
app_name = 'AppLogin'
urlpatterns = [
    path('signup/', views.signupUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/', views.editprofileUser, name='editprofile'),
]