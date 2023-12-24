import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = 'global'
        self.room_group_name = self.room_name
        print("Somebody joined group")
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type":"chat_message",
                "room_id":"something",
                "username":"username",
                "message":{
                    "notify":True,
                    "text":"Somebody joined the chat"
                },
            }
        )

        
    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )              
    def receive(self, text_data):
        jsonMessage = json.loads(text_data)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type":"chat_message",
                "room_id":jsonMessage["room_id"],
                "username":jsonMessage["username"],
                "message":jsonMessage["message"],
            }
        )
    def chat_message(self, event):
        self.send(text_data=json.dumps({
                "room_id":event["room_id"],
                "username":event["username"],
                "message":event["message"]}))   