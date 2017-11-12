from threading import Thread
import socket

addr = ("127.0.0.1", 8005)
Sock = socket.socket()
Sock.bind(addr)
Sock.listen(10)
clientAddr = []
clientSock = []


# Поток обрабатывает новое соединение и создает для нового клиента поток
class ThreadAccept(Thread):
    def __init__(self, sock):
        Thread.__init__(self)
        self.sock = sock
    def run(self):
        print("Accept thread run")
        while True:
            s, addres = self.sock.accept()
            print("Connect: " + addres[0] + " " + str(addres[1]))
            clientAddr.append(addres)
            clientSock.append(s)
            p = ThNewClient(s)
            p.start()


# Поток для клиента слушает сообщение и отпраляет и всем
class ThNewClient(Thread):
    def __init__(self, sock):
        Thread.__init__(self)
        self.sock = sock
    def run(self):
        print("New thread for client run")
        while True:
            data = self.sock.recv(4096)
            print(data.decode("utf-8"))
            for s in clientSock:
                s.send(data)



if __name__ == "__main__":
    try:
        p1 = ThreadAccept(Sock)
        p1.start()
    except BaseException:
        print("Socket close except")
        Sock.close()