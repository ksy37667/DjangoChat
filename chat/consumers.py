import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # 대화방에 참여한다.
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def  disconnect(self, close_code):
        # 대화방에서 나간다.
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # 웹소켓으로부터 메세지를 받는다
    async def  receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # 대화방으로 메세지를 보낸다.
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # 대화방으로부터 메세지를 받는다.
    async def  chat_message(self, event):
        message = event['message']

        # 웹소켓으로 메세지를 보낸다.
        await self.send(text_data=json.dumps({
            'message': message
        }))