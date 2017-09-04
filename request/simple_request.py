import requests
url = "http://api.icndb.com/jokes/random"
answ = requests.get(url)
print(answ.json())
print("Соединение успешно/не успешно -->" + answ.json()["type"])
print("Шутка про Чак Норриса --> " + answ.json()["value"]["joke"])
