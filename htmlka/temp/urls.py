from django.urls import path
from temp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('register/', views.UserRegister.as_view(), name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('account/', views.account, name='account'),
]