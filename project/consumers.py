import json

from asgiref.sync import async_to_sync
from channels.consumer import AsyncConsumer
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        await self.send({
            "type": "websocket.accept"
        })
        self.room_group_name = 'chat_room'
        self.room_name = 'room'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

    async def websocket_receive(self,event):
        text_data_json = json.loads(event.get('text'))
        message = text_data_json['message']
        person1 = text_data_json['person1']
        id = text_data_json['id']
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'text':message,
                'id':id,
                'person1':person1,
            }
        )

    async def websocket_disconnect(self,event):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def chat_message(self, event):
        print(event)
        await self.send({
            'type':'websocket.send',
            'text':str('/'.join([
                event.get('id'),
                event.get('text'),
                event.get('person1'),
            ]))
        })

class EnterConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connection")
        await self.send({
            "type": "websocket.accept"
        })
        self.room_group_name = 'enter_room2'
        self.room_name = 'room2'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

    async def websocket_receive(self, event):
        print("event")
        text_data_json = json.loads(event.get('text'))
        message = text_data_json['text']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'text': message
            }
        )

    async def websocket_disconnect(self, event):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def chat_message(self, event):
        await self.send({
            'type': 'websocket.send',
            'text': event.get('text')
        })