from modules import external
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time
from random import randint


cred = credentials.Certificate('secret.json')
default_app = firebase_admin.initialize_app(cred,  {'databaseURL': 'https://cultivatetheworld-d01f7.firebaseio.com/m'})
root = db.reference("")

def start():
    while True:
        root.update({"temp": external.get_temp()})
        root.update({"altitude": external.get_altitude()})
        root.update({"pressure": external.get_pressure()})
        root.update({"humidity": external.get_humidity()})

        # root.update({"temp": randint(0, 10)})
        # root.update({"altitude": randint(0, 10)})
        # root.update({"pressure": randint(0, 10)})
        # root.update({"humidity": randint(0, 10)})

        time.sleep(5)


if __name__ == "__main__":
    start()
