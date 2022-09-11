from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm
# rooms =[
#     {'id': 1, 'name': 'fronted'},
#     {'id': 2, 'name': 'backend'},
#     {'id': 3, 'name': 'python'},
#     {'id': 4, 'name': 'django'},
#     {'id': 5, 'name': 'javascript'},
# ]
def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    ctx = {'room': room}
    return render(request, 'base/room.html', ctx)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
        
    context = {'obj': room}
    return render(request, 'base/delete.html', context)