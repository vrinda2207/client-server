import socket
max=80
port=8080
def func(connfd):
    while True:
        data=connfd.recv(max).decode()
        if not data:
            break
        print(f"from client {data}\n to client",end='')
        msg=input()
        connfd.send(msg.encode())
        if msg.strip().lower()=='exit':
            print("server exiting")
            break
sockfd=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sockfd.bind(('0.0.0.0',port))
sockfd.listen(5)
print("server listening")
connfd,addr=sockfd.accept()
print(f"accepted client :{addr}")
func(connfd)
sockfd.close()
