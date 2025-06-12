import asyncio
import tornado.ioloop
import tornado.websocket

class WebSocketClient:
    def __init__(self, url):
        self.url = url
        self.ws = None

    async def connect(self):
        self.ws = await tornado.websocket.websocket_connect(self.url)
        print("Connected to the server.")
        await self.run()

    async def run(self):
        while True:
            message = input("Enter message to send (type 'exit' to disconnect): ")
            await self.ws.write_message(message)

            if message.lower() == 'exit':
                print("Disconnecting from server.")
                self.ws.close()
                break

            response = await self.ws.read_message()
            print(f"Received from server: {response}")

if __name__ == "__main__":
    url = "ws://localhost:65432/ws"
    asyncio.get_event_loop().run_until_complete(WebSocketClient(url).connect())
