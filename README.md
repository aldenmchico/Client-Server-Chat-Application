# Client Server Chat Application
For this project, I created a simple client-server chat application using Python sockets on a persistent TCP connection. Because no EOT byte is sent using sockets, a zero-padded 5 digit number is prepended to each message to indicate the length of the message in bytes. The receiver of the message uses this information to know how many bytes it expects to receive and properly decode the received message from the byte stream.
<br/><br/>
<h2>Testing the Program</h2>
To test out my program download the repository and run <b>server.py</b> on one terminal and <b>client.py</b> on another terminal. The client terminal connects to the server terminal using port 4000 and communication between the two can be initiated by sending messages between the two running programs.

