import tweepy				# модуль для работы с твиттером
def twitter_api():			# функция в которой мы авторизуемся в твиттере
    consumer_key = "you consumer_key"
    consumer_secret_key = "you consumer_secret_key"
    access_key = "you access_key "
    access_secret_key = "you access_secret_key"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_key, access_secret_key)
    api = tweepy.API(auth)
    return api 				# возвращаем объект для работы с твиттером

 api = twitter_api()		# авторизация и получаем тот самый объект

api.update_status(status="twit")                # написать твит
api.update_with_media(status="текст",
                      filename="путь до медиа объекта")        # твит с картинкой/гифкой
api.create_friendship()                         # зафрендить по id/screen_name/user_id
api.destroy_friendship()                        # отписаться по id/screen_name/user_id
followers = api.followers()                     # получить список фолловеров
friends = api.friends()                         # получить список читаемых	

for i in friends:                               # Пример пройдемся по читаемым и узнаем о них все
    print(i.screen_name)                        # получить ник
    print(i.name)                               # получить имя
    print(i.location)                           # получить расположение
    print(i.description)                        # получить описание профиля
    print(i.followers_count)                    # получить список подписчиков
    print(i.friends_count)                      # получить список читаемых
    print("===================")

news = api.home_timeline()                      # получить новостую ленту
for i in news:                                  # Пример пробежимся по новым твитам и узнаем о них все
    print(i.text)                               # получить текст твита
    print(i.id)                                 # получить id твита
    print(i.user.name)                          # получить имя написавшего этот твит
    print(i.created_at)                         # получить дату создания твита
    print(i.retweet_count)                      # получить кол-во ретвитов
    print("=====================")

twit = api.user_timeline("@elonmusk")           # получить список твитов @elonmusk
for i in twit:                                  # переберем этот список и узнаем текст твита и кол-во ретвитов
    print(i.text)
    print(i.retweet_count)
    print("=====================")

friends = api.friends()                         # получить список читаемых
for i in friends:                               # пробежимся по читаемым
    print(i.name)                               # узнаем имя
    for j in api.user_timeline(i.screen_name):  # и пробежимся по его твитам
        print(j.text)                           # выведим твит
        if "погода" in j.text:                  # если в тексте твита есть слово погода
            api.retweet(j.id)                   # реттвитим его себе
