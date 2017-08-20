import pyowm
import time
import datetime
city = input("Введите город\n")
#city = "Pinsk"
now_day = datetime.date.today()                                       # Получить дату в формате год-месяц-число
now_time = datetime.datetime.now()                                    # получить время
print(now_day)                                                        # выводим дату
print(now_time.hour)                                                  # выводим часы
print(now_time.minute)                                                # выводим минуты
print(time.strftime("%X"))                                            # время в формате часы минуты секунды
key = pyowm.OWM("key", language="ru")    # с помощью ключа конектимся к севреру погоды
weather = key.weather_at_place(city)                                  # получаем объект в котором вся информация о погоде в city
weather = weather.get_weather()                                       #
print(weather.get_temperature("celsius")["temp"])                     # получить среднюю температуру
print(wweather.get_temperature("celsius")["temp_max"])                # получить максимальную температуру
print(weather.get_temperature("celsius")["temp_min"])                 # получить минимальную температуру
print(str(weather.get_reference_time(timeformat="date")))             # дата время
print(str(weather.get_detailed_status()))                             # облачно/пасмурно/дождливо/идет снег
print(str(weather.get_wind()["speed"]))                               # получить скорость ветра
print(str(weather.get_humidity()))                                    # получить влажность
print(str(weather.get_sunrise_time("iso")))                           # время дата
print ("В городе " + city + " сейчас " + str(weather.get_detailed_status())
       + " температура " + str(weather.get_temperature("celsius")["temp"]) + " градусов\nвлажность "
       + str(weather.get_humidity()) + "% скорость ветра " + str(weather.get_wind()["speed"]) + " м/c")
