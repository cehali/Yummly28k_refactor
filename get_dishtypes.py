import json

with open('recipes.json') as json_data:
    d = json.load(json_data)

temp = []
for n in range(1, 9):
    cour = d.get('meta0000'+str(n)).get('attributes').get('cuisine')
    for c in cour:
        temp.append(str(c))

for n in range(10, 99):
    cour = d.get('meta000'+str(n)).get('attributes').get('cuisine')
    for c in cour:
        temp.append(str(c))

for n in range(100, 999):
    cour = d.get('meta00'+str(n)).get('attributes').get('cuisine')
    for c in cour:
        temp.append(str(c))

for n in range(1000, 9999):
    cour = d.get('meta0'+str(n)).get('attributes').get('cuisine')
    for c in cour:
        temp.append(str(c))

for n in range(10000, 27638):
    cour = d.get('meta'+str(n)).get('attributes').get('cuisine')
    for c in cour:
        temp.append(str(c))

'''Lunch_Snacks = 0
Beverages = 0
Breakfast_Brunch = 0
Condiments_Sauces = 0
Soups = 0
Main_Dishes = 0
Appetizers = 0
Cocktails = 0
Desserts = 0
Side_Dishes = 0
Afternoon_Tea = 0
Breads = 0
Salads = 0

for tmp in temp:
    if tmp == 'Lunch and Snacks':
        Lunch_Snacks += 1

    if tmp == 'Beverages':
        Beverages += 1

    if tmp == 'Breakfast and Brunch':
        Breakfast_Brunch += 1

    if tmp == 'Condiments and Sauces':
        Condiments_Sauces += 1

    if tmp == 'Soups':
        Soups += 1

    if tmp == 'Main Dishes':
        Main_Dishes += 1

    if tmp == 'Appetizers':
        Appetizers += 1

    if tmp == 'Cocktails':
        Cocktails += 1

    if tmp == 'Desserts':
        Desserts += 1

    if tmp == 'Side Dishes':
        Side_Dishes += 1

    if tmp == 'Afternoon Tea':
        Afternoon_Tea += 1

    if tmp == 'Breads':
        Breads += 1

    if tmp == 'Salads':
        Salads += 1

print Lunch_Snacks
print Beverages
print Breakfast_Brunch
print Condiments_Sauces
print Soups
print Main_Dishes
print Appetizers
print Cocktails
print Desserts
print Side_Dishes
print Afternoon_Tea
print Breads
print Salads'''

print list(set(temp))