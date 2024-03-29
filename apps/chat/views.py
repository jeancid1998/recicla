
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def indexchat(request):
    return render(request, 'recicla/chat.html', {})

def room(request, room_name):
    return render(request, 'recicla/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })