#%%
import socket;


def server():

  serverSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  serverSocket.bind((socket.gethostname(),1234,))
  serverSocket.listen(5)
  while True:
    conn, addr = serverSocket.accept()
    print('connect from', addr)
    data=conn.recv(1024)
    conn.send(data)
    conn.close()
  serverSocket.close()
if __name__ == "__main__":
    server()

# %%
