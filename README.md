## Socket server/client

The server is written in Java
The client is writtern in Python


When a server instance is created in Java, the instance will spawn worker threads for each incoming connection.

The socket communication is thread safe because of the observer pattern. The main thread is blocked until the server is shutdown. 

All code execution is offloaded to worker threads in the form of listeners. The worker will be notified when it should excecute a listener.

Listeners will block worker threads. 