import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from nltk import pos_tag, word_tokenize, download, help


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["roomname"]
        self.nickname = self.scope["url_route"]["kwargs"]["nickname"]
        self.room_group_name = self.room_name
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
                    "text":self.nickname + "joined the chat"
                },
            }
        )

        
    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )              
    def receive(self, text_data):
        jsonMessage = json.loads(text_data)
        if(jsonMessage["message"]["text"].startswith(":tokenise:")):
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type":"nltk_message",
                    "room_id":jsonMessage["room_id"],
                    "username":jsonMessage["username"],
                    "message":jsonMessage["message"],
                }
            )
        else:
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
    def nltk_message(self, event):
        baseText = event["message"]["text"]
        if(type(event["message"]["text"]) != dict):
            baseText = baseText.lstrip(":tokenise:")
            tokenisedString =''
            try:
                tokenisedString = pos_tag(word_tokenize(baseText))
            except:
                import nltk
                nltk.download('averaged_perceptron_tagger')
                tokenisedString = pos_tag(word_tokenize(baseText))
            finally:
                jsonObj = {}
                for i in tokenisedString:
                    jsonObj[i[0]] = i[1]
                event["message"]["text"] = jsonObj
        self.send(text_data=json.dumps({
                "room_id":event["room_id"],
                "username":event["username"],
                "message":event["message"]}))           