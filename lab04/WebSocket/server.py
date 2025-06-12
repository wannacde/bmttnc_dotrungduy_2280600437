import asyncio
import tornado.web
import tornado.websocket

# Define WebSocket handler
class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print(f"Client connected: {self.request.remote_ip}")

    def on_message(self, message):
        print(f"Received from client: {message}")

        if message.lower() == 'exit':
            self.write_message("Server: Connection closing as per your request.")
            print("Client requested to close connection.")
            self.close()
        else:
            self.write_message(f"Server echo: {message}")

    def on_close(self):
        print(f"Connection closed.")

# Define Tornado application
def make_app():
    return tornado.web.Application([
        (r"/ws", EchoWebSocket),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(65432)
    print("Starting WebSocket server on ws://localhost:65432")
    asyncio.get_event_loop().run_forever()
