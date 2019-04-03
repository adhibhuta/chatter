from simple_websocket_server import WebSocketServer, WebSocket
from chatbot import get_response


class ChatServer(WebSocket):

    def handle(self):
        message = self.data
        response = get_response(message)
        self.send_message(response)

    def connected(self):
        print(self.address, 'connected')

    def handle_close(self):
        print(self.address, 'closed')



server = WebSocketServer('', 8000, ChatServer)
server.serve_forever()
