from django.shortcuts import render, redirect


def chatPage(request, *args, **kwargs):
    context = {}
    return render(request, 'chat/player_chat.html', context)


def home(request):
    return render(request, 'registration/home.html')

