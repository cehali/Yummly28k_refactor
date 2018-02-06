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


'''import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

with open('recipes_withDishType_withoutParent.json') as json_data:
    recipes_data = json.load(json_data)

# Use a service account
cred = credentials.Certificate('reciperecommender-a2348-firebase-adminsdk-y153k-b5e35e8df0.json')
firebase_admin.initialize_app(cred)

db = firestore.client()'''

list_recipes = []

'''for n in range(1, 10):
    rcp = {}
    rcp['meta0000'+str(n)] = recipes_data.get('meta0000'+str(n))
    list_recipes.append(rcp)

for n in range(10, 100):
    rcp = {}
    rcp['meta000'+str(n)] = recipes_data.get('meta000'+str(n))
    list_recipes.append(rcp)

for n in range(100, 1000):
    rcp = {}
    rcp['meta00'+str(n)] = recipes_data.get('meta00'+str(n))
    list_recipes.append(rcp)

for n in range(1000, 10000):
    rcp = {}
    rcp['meta0'+str(n)] = recipes_data.get('meta0'+str(n))
    list_recipes.append(rcp)'''

for n in range(22291, 27639):
    rcp = {}
    rcp['meta'+str(n)] = recipes_data.get('meta'+str(n))
    list_recipes.append(rcp)


for lr in list_recipes:
    root = db.reference('/')
    new_user = root.set(lr.values()[0])
    '''doc_ref = db.collection(u'recipes').document(lr.keys())
    doc_ref.set(lr.values())'''
