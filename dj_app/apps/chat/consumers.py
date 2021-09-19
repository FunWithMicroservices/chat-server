from channels.generic.websocket import AsyncJsonWebsocketConsumer


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def websocket_connect(self, event):
        thread_id = self.scope["url_route"]["kwargs"]["thread"]
        await self.channel_layer.group_add(
            f"thread_{thread_id}",
            self.channel_name
        )

        await self.accept()

        await self.send_json(content={})

    async def websocket_receive(self, event):
        # Not Required - We won't receive sth. from user
        pass

    async def websocket_disconnect(self, event):
        pass

    async def send_message(self, event):
        # triggered from post save signal
        await self.send_json(content=event["context"])
