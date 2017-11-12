#===========================================
# Это код клиента, название файлов перепутал
#=========================================== 
from threading import Thread
import socket
from tkinter import *
addr = ("127.0.0.1", 8005)
Socket = socket.socket()
Socket.connect(addr)
SocketForSend = socket.socket()
SocketForSend.connect(addr)

# Функция слушает сокет и если есть сообщение пишет его в поле text
def sen(sock):
    data = sock.recv(12000)
    data = data.decode("utf-8")
    data = data + "\n"
    text.insert(END, data)
# событие считывает с поля entry сообщение и посылает его на сервер
def click(event):
    data = ent.get()
    data = data.encode()
    Socket.send(data)

# поток слушающий сообщения
class Threcv(Thread):
    def __init__(self, sock):
        Thread.__init__(self)
        self.sock = sock
    def run(self):
        while True:
            sen(self.sock)

# делаем GUI =================
chat = Tk()
chat.title("Chat")
text = Text(chat, width=40, font="Verdana 12", wrap=WORD, bd=2)
bt = Button(chat, text = "Отправить")
ent = Entry(chat, width = 30, bd = 2)
ent.grid(row = 1, column = 0, padx = 10, pady = 4)
text.grid(row = 0, column = 0, padx = 10, pady = 5)
bt.grid(row = 2, column = 0, padx = 10, pady = 3)
bt.bind("<Button-1>", click)
bt.bind("<Return>", click, "+")
# =============================

if __name__ == "__main__":
    try:
        #  Создаем поток
        th = Threcv(Socket)
        # Запускаем его
        th.start()
        # Запускаем GUI
        chat.mainloop()
    # В случае любой ошибки закрываем соединение
    except BaseException:
        print("Socket close except")
        Socket.close()



