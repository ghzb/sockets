class SocketListener:

    class ObserverRegistration:
        observer = None
        channel = None
        def __init__(self, channel, observer):
            self.observer = observer
            self.channel = channel

    listeners = []

    def register(self, channel, observer):
        self.listeners.append(SocketListener.ObserverRegistration(channel, observer))

    def notify(self, data):
        for listener in self.listeners:
            if (listener.channel == data.channel):
                listener.observer(data)