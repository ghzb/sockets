from sockets import SocketClient

def prompt():
    print('> ', end='')
    return input()

def output(data):
     print("\r< " + data + "\n> ", end='')


client = SocketClient('localhost', 8888)
client.on("$MESSAGE", lambda data: output(data.message))
client.on("$CONNECT", lambda data: output("CONNECTED"))
client.on("$DISCONNECT", lambda data: print('Bye!'))
client.on("$ISSUE", lambda data: output(data.error))

while client.connected:
    cmd = prompt()
    if (cmd == 'quit' or cmd == 'exit'):
        client.disconnect()
    elif (cmd == 'help'):
        print('quit|exit - disconnect from socket server')
        print('sendLoop  - send a loop of data to server')
        print('getLoop   - get a loop of data from server')
        print('help      - show this menu')
        print('<any>     - send anything to the server')
    elif (cmd == 'sendLoop'):
        for i in range(10000):
            client.send(i)
    else:
        client.send(cmd)