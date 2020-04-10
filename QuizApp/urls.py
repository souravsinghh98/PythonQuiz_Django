from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('addQues/',views.add,name='addQues'),
    path('test/',views.test,name='test'),
    path('result/',views.result,name='result'),
    path('register/',views.UserRegistration,name='register'),
    path('login/',views.UserLogin,name='login'),
    path('logout/',views.UserLogout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('change_pic/',views.profile_pic,name='change_pic'),
    path('leader/<str:pk>/',views.leader_profile,name='leader'),

    #password reset
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='QuizApp/password_reset.html')
    ,name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='QuizApp/password_reset_sent.html'),
     name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='QuizApp/password_reset_form.html'),
     name='password_reset_confirm'),
    path('reset_password_success/', auth_views.PasswordResetCompleteView.as_view(template_name='QuizApp/password_reset_sucess.html'),
     name='password_reset_complete'),

]