import socket
addres = ("127.0.0.1", 8080)                    # создаем кортеж из ip и порта
sock = socket.socket()                          # создаем объект сокет
sock.bind(addres)                               # привязываем сокет к нашему ip и порту
print("=== server start on port 8080 ===")
sock.listen(1)                                  # говорим серверу максимальное кол-во подключений
so, addr = sock.accept()                        # ждем соединения, возвращает кортеж из ip и порта клиента, и сокет
data = so.recv(1024)                            # слушаем клиента
data = data.decode("utf-8")                     # декодируем поток байтов
print(data)
data = data + " " + addr[0]                     # готовим сообщения для клиента
data = data.encode()                            # готовим сообщение к отправке т.к. сокеты работают с байтами
so.send(data)                                   # отправляем сообщение
so.close()