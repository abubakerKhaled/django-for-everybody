"""
Establish a socket connection to a web server and retrieve a web page.

This function creates a socket connection to 'data.pr4e.org' on port 80,
sends an HTTP GET request for 'page1.html', and prints the received data.

Parameters:
    None

Returns:
    None

Raises:
    Exception: If the connection fails or an error occurs during the process.
"""

import socket

try:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect(("data.pr4e.org", 80))
    cmd = 'GET http://data.pr4e.org/page1.html HTTP/1.0\r\n\r\n'.encode()
    socket.send(cmd)
    
    while True:
        data = socket.recv(512)
        if data < 1:
            break
        print(data.decode(), end='')
    
except Exception:
    print("Connection failed...")
