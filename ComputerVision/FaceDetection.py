import numpy as np
import cv2
# import tweepy
# def twitter_api():
#     consumer_key = "your consumer_key"
#     consumer_secret_key = "your consumer_secret_key"
#     access_key = "yout access_key"
#     access_secret_key = "your access_secret_key"
#     auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
#     auth.set_access_token(access_key, access_secret_key)
#     api = tweepy.API(auth)
#     return api
#
# api = twitter_api()
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while (True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    if len(faces) > 0:
        print("find {0} faces".format(len(faces)))
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#        cv2.imwrite("user." + "jpg", gray[y:y + h, x:x + w])
#        api.update_with_media(filename="/Users/ivan/PycharmProjects/untitled/user.jpg", status="Detect")
#        break
    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()