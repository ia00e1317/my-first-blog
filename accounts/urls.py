from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    
    path('password_change/', views.PasswordChange.as_view(), name='password_change'), #追加
    path('password_change/done/', views.PasswordChangeDone.as_view(), name='password_change_done'), #追加
]
