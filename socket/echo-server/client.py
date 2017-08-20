import socket
addres = ("127.0.0.1", 8080)    # создаем кортеж из ip и порта
sock = socket.socket()          # создаем объект сокет
sock.connect(addres)            # устанавливаем связь между нашим сокетом и сервером
data = "ping"                   # сообщение
data = data.encode()            # переводим в байты так как сокеты работают с потоком байт
sock.send(data)                 # отправляем сообщение на сервер
data = sock.recv(1024)          # ждем ответа
data = data.decode("utf-8")     # декодируем поток байтов
print(data)
sock.close()                    # закрываем соединение
