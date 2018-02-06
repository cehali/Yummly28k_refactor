import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

with open('recipes_withDishType_withoutParent_specialIndex_3.json') as json_data:
    recipes_data = json.load(json_data)

cred = credentials.Certificate('reciperecommender-a2348-firebase-adminsdk-y153k-b5e35e8df0.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://reciperecommender-a2348.firebaseio.com/'
})


ref = db.reference('/recipes')
data = ref.get()

print data.get('meta00001')