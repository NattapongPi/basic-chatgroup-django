from django.urls import path

from . import views

app_name = 'chatroom'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('chat/<int:room_id>', views.chat, name='chat'),
    path('chat/<int:room_id>/send', views.send, name='send'),
    path('create/', views.create, name='create'),
    path('createRoom/', views.createRoom, name='createRoom'),
    path('register/', views.register, name='register'),
    path('createUser/', views.createUser, name='createUser'),
    path('login/', views.login, name='login'),
    path('loginRequest/', views.loginRequest, name='loginRequest'),
    path('logout/', views.logout, name='logout'),
    path('', views.index, name='index'),
]
