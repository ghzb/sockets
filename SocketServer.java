import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

class SocketServer {
    private static Socket socket;
    private static ServerSocket server;

    public static void main(String[] args) {

        try
        {
            server = new ServerSocket(8888);

            System.out.println("listening... "  + 8888);

            while (true)
            {
                socket = server.accept();
                System.out.println("connected");

                DataInputStream input = new DataInputStream(socket.getInputStream());
                BufferedReader reader = new BufferedReader(new InputStreamReader(input));

                DataOutputStream output = new DataOutputStream(socket.getOutputStream());

                String text;

                do {
                    text = reader.readLine();
                    output.writeUTF(text + "\n");
                    System.out.println(text);
                } while(!text.equals("bye"));

                output.writeUTF(text + "disconnected\n");
                socket.close();
                System.out.println("disconnected");
            }
        }catch (IOException err)
        {
            System.out.println("Server Exception: " + err.getMessage());
            err.printStackTrace();
        }

    }
}