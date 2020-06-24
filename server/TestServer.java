public class TestServer {

    private static void onMessage (SocketData socket) {
        if (socket.message == null)
        {
            return;
        }
        if (socket.message.equals("getLoop"))
        {
            for(int i = 0; i<=10000;i++)
            {
                socket.worker.send("$MESSAGE", String.valueOf(i));
            }
        } else {
            socket.worker.send(socket.channel, socket.message);
        }
    }

    private static void onDisconnect (SocketData socket) {
        System.out.println("DISCONNECT");
    }

    private static void onConnect (SocketData socket) {
        System.out.println("CONNECT");
    }

    private static void onIssue (SocketData socket) {
        socket.error.printStackTrace();
    }

    public static void main(String[] args) {
        SocketServer server = new SocketServer();
        server.on("$CONNECT", TestServer::onConnect);
        server.on("$MESSAGE", TestServer::onMessage);
        server.on("$DISCONNECT", TestServer::onDisconnect);
        server.on("$ISSUE", TestServer::onIssue);
        System.out.println("Waiting for first connection...");
        while (true){
            server.waitForConnection();
            System.out.println("Open for another connection");
        }
    }
}
