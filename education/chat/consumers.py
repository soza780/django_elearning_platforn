import json
from channels.generic.websocket import WebsocketConsumer


class ChatConsumers(WebsocketConsumer):

    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass  # i don't know why should i pass this , check documents. WTH ... documents says when
        # a websocket close, you don't need to do anything...

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        self.send(text_data=json.dumps({"message": message}))
