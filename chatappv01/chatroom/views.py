from django.core.checks import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from chatroom.models import Room, Message


def index(request):
    context = {}
    return render(request, 'index.html', context)


def home(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms,
    }
    return render(request, 'home.html', context)


def chat(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    messages = Message.objects.filter(room=Room.objects.get(pk=room_id))
    print(messages)
    context = {
        'roomname': room.roomname,
        'room_id': room.id,
        'messages': messages,
    }
    return render(request, 'chat.html', context)


def create(request):
    context = {}
    return render(request, 'create.html', context)


def createRoom(request):
    roomname = request.POST['roomname']
    print(roomname)
    Room.objects.create(roomname=roomname)
    return HttpResponseRedirect(reverse('chatroom:home'))


def send(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    message = request.POST['message']
    sender = request.POST['sender']
    Message.objects.create(
        message=message,
        sender=sender,
        room=room,
    )
    return HttpResponseRedirect(reverse(
        'chatroom:chat',
        args=(room_id,)
    )
    )


def register(request):
    context = {}
    return render(request, 'register.html', context)


def login(request):
    context = {}
    return render(request, 'login.html', context)


def createUser(request):
    username = request.POST['username']
    password = request.POST['password']
    repassword = request.POST['repassword']
    if password == repassword:
        user = User.objects.create_user(
            username=username,
            password=password,
        )
        user.save()
        auth_login(request, user)
        return HttpResponseRedirect(reverse('chatroom:home'))
    return HttpResponseRedirect(reverse('chatroom:register'))


def loginRequest(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(
        request,
        username=username,
        password=password,
    )

    if user is not None:
        auth_login(request, user)
        return HttpResponseRedirect(reverse('chatroom:home'))

    else:
        return HttpResponseRedirect(reverse('chatroom:login'))


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('chatroom:index'))
