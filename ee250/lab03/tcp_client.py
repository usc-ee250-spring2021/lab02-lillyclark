"""
Server IP is TODO, ports are 5000-5008, socket is UNIX TCP 
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
You may want to use the python "input" and "encode" functions
Establish a socket connection -> send a short message -> get a message back -> ternimate
"""
import socket

def main():

    HOST = '34.209.114.30'
    HOST = '127.0.0.1'
    PORT = 5004

    # TODO: Create a socket and connect it to the server at the designated IP and port
    
    # TODO: Get user input and send it to the server using your TCP socket
    
    # TODO: Receive a response from the server and close the TCP connection

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print('Enter your message:')
        msg = input()
        s.sendall(msg.encode())
        data = s.recv(1024)

    print('Received', repr(data))

if __name__ == '__main__':
    main()
