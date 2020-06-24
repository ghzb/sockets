import threading

from .SocketData import SocketData

class SocketWorker (threading.Thread):
    socket = None
    listener = None
    def __init__(self, socket, listener):
        super().__init__()
        self.socket = socket
        self.listener = listener

    def waitForResponse(self):
        res = ""
        while True:
            _in = self.socket.recv(1).decode('utf-8')
            if _in == "\n":
                break
            else:
                res += _in
        return res
    
    def run(self):
        while True:
            try:
                encoded = self.waitForResponse()
                data = SocketData.parse(encoded)
                self.listener.notify(data)
            except:
                break