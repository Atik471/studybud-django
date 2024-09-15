from django.shortcuts import render
from .models import Room

# rooms=[]

# rooms = [
#     {'id': 1, 'name': "Let's learn python"},
#     {'id': 2, 'name': "Let's learn Java"},
#     {'id': 3, 'name': "Let's learn Javascript"}, 
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)

    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    
    context = {'room': room}

    return render(request, 'base/room.html', context)