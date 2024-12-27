import socket
port=8080
max=80
sockfd=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sockfd.connect(('127.0.0.1',port))
while True:
    msg=input("to server:")
    sockfd.send(msg.encode())
    data=sockfd.recv(max).decode()
    print(f"from server :{data}")
    if data.strip().lower()=='exit':
        print("server exited closing connection")
        break
sockfd.close()
