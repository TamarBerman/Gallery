import json
from channels.generic.websocket import AsyncWebsocketConsumer
''' base class AsyncWebSocketConsumer allows the Django project to handle the WebSocket'''
class ChatConsumer(AsyncWebsocketConsumer):
    
    
    async def connect(self):
        # retrieves the username of the currently authenticated user from the scope and assigns it to the sender attribute of the ChatConsumer instance
        self.sender = self.scope['user'].username
        # gets the username from the URL route’s keyword arguments and assigns it to the recipient attribute of the ChatConsumer instance
        self.recipient = self.scope['url_route']['kwargs']['username']

        # a group is a named collection of channels (users) .
        self.room_group_name = "group_chat"
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        # build the WebSocket connection
        await self.accept()


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )


    async def receive(self, text_data):
        #  parsing the JSON data into Python dictionary
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
    
        # broadcasting a message 
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': self.sender
            }
        )
    
    # handle the message received by the group and extract the message and sender details from the event
    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']
      
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender
        }))


