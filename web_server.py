from socket import *

def create_server():
    ## Create a socket 
    server_socket = socket(AF_INET, SOCK_STREAM)
    try:
        ## Define the server address and port
        server_socket.bind(('localhost', 9000))
        server_socket.listen(5)
        while(1):
            (client_socket, address) = server_socket.accept()
            
            rd = client_socket.recv(5000).decode()
            pieces = rd.split('\n')
            if (len(pieces) > 0) : print(pieces[0])
            
            data = 'HTTP/1.0 200 OK\r\n'
            data += 'Content-Type: text/html; charset=utf-8\r\n'
            data += '\r\n'
            data += '<html><body><h1>Hello, world!</h1></body></html>'
            client_socket.sendall(data.encode())
            client_socket.shutdown(SHUT_WR)
            
    except KeyboardInterrupt:
        print('\nShutting down server...\n')
    except Exception as exp:
        print('Error:\n')
        print(exp)
    
    server_socket.close()

print('Accessing http://localhost:9000')
create_server()