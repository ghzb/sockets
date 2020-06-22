import socket
import sys

class SocketClient ():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    responses = []
    endl = '\n'
    connected = False

    def __init__(self, host, port, endl='\n'):
        self.connect(host, port)
        self.endl = endl

    def send(self, msg):
        data = str(msg) + self.endl
        self.sock.sendall(data.encode())
        self.responses.append(self._receive())

    def connect(self, host, port):
        if not self.connected:
            self.sock.connect((host, port))
            self.connected = True

    def disconnect(self):
        if self.connected:
            self.send('bye')
            self.sock.close()
            self.connected = False

    def _receive(self):
        res = ""
        while True:
            _in = self.sock.recv(1).decode('utf-8')
            if _in == self.endl:
                break
            else:
                res += _in
        return res

    def getResponse(self):
        res = self.responses
        self.responses = []
        return list(res)


client = SocketClient('localhost', 8888)
try:
    while client.connected:
        print('> ', end='')
        msg = input()

        if (msg == 'quit' or msg == 'bye'):
            client.disconnect()

        elif (msg == 'loop'):
            for i in range(10000):
                client.send(i)
        else:
            client.send(msg)


        for res in client.getResponse():
            response = "<" + res
            print(response)

finally:
    client.disconnect()