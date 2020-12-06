import socket
def client():
  clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  clientSocket.connect((socket.gethostname(),1234,))
  clientSocket.send(b'Hello,world')
  data=clientSocket.recv(1024)
  print('receive:', data)
  clientSocket.close()
if __name__ == "__main__":
    client()