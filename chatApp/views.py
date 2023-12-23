from django.shortcuts import render,HttpResponse

def index(request):
    return render(request, 'index.html')

def chatroom(request):
    print(request.path)
    return render(request, 'chatroom.html')