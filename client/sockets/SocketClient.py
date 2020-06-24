import socket

from .SocketData import SocketData
from .SocketListener import SocketListener
from .SocketWorker import SocketWorker

class SocketClient ():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener = None
    connected = False
    worker = None

    def __init__(self, host, port):
        self.listener = SocketListener()
        self.connect(host, port)
        

    def send(self, message, channel="$MESSAGE"):
        data = SocketData(message, channel)
        self.sock.sendall((data.serialize() + "\n").encode())
    
    def connect(self, host, port):
        if not self.connected:
            self.sock.connect((host, port))
            self.connected = True
            self.host = host
            self.port = port
            self.worker = SocketWorker(self.sock, self.listener)
            self.worker.start()

    def disconnect(self):
        if self.connected:
            try:
                self.send('bye', "$DISCONNECT")
                self.sock.close()
            finally:
                self.connected = False
                self.listener.notify(SocketData(None, '$DISCONNECT'))

    def on(self, channel, observer):
        self.listener.register(channel, observer)