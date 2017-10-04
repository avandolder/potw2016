# Import the socket library, to enable access to low-level TCP communication.
import socket

# Open a socket communicating with potw.quinnftw.com on port 80.
s = socket.create_connection(('potw.quinnftw.com', 80))

# Send a basic GET request on the socket for the secret message page.
s.sendall(b'GET /problem/s3cret HTTP/1.1\r\nHost: potw.quinnftw.com\r\n\r\n')

# Receive up to 10000 bytes from the socket, convert it into a UTF-8 string, then output it.
print(s.recv(10000).decode('utf-8'))
