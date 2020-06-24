import base64

class SocketData ():
    channel = ""
    message = ""

    def __init__(self, message, channel="$MESSAGE"):
        self.channel = channel
        self.message = message

    @staticmethod
    def parse(data):
        if isinstance(data, str):
            data = data.encode()
        ddata = base64.decodebytes(data).decode()
        channel, message = ddata.split(':', 1)
        return SocketData(message, channel)

    def serialize(self):
        return base64.b64encode((self.channel + ":" + str(self.message)).encode()).decode()

    def __str__(self):
        return self.channel + ": " + str(self.message.encode())