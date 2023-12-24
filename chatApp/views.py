from django.shortcuts import render,HttpResponse

def index(request):
    return render(request, 'index.html')

def chatroom(request, roomname, nickname):
    context = {"chatroom":roomname, "nickname":nickname}
    return render(request, 'chatroom.html', context)