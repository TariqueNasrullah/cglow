from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
import time
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import asyncio

def index(request):
    group_name = 'chat_lobby'
    message = 'triggered hello'

    async_to_sync(msend)(group_name, message)

    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

async def msend(group_name, message):
    channel_layer = get_channel_layer()

    await channel_layer.group_send(
        '{}'.format(group_name),
        {
            'type': 'chat_message',
            'message': message
        }
    )