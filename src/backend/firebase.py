
import firebase_admin
from firebase_admin import credentials, db

from pathlib import Path

root = Path(__file__).parent.parent.parent


def init():
    cred = credentials.Certificate(str(root / "cityhack21-firebaseAdmin.json"))
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://cityhack21-6404b-default-rtdb.firebaseio.com/'
    })


def get_data(key):
    return db.reference(key).get()


def set_data(key, value):
    return db.reference(key).update(value)

init()
