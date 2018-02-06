import json
from collections import Counter

with open('recipes_withDishType_withoutParent_specialIndex_3.json') as json_data:
    recipes_data = json.load(json_data)


courses = ['Lunch and Snacks',
                    'Beverages',
                    'Breakfast and Brunch',
                    'Condiments and Sauces',
                    'Soups',
                    'Main Dishes',
                    'Appetizers',
                    'Cocktails',
                    'Desserts',
                    'Side Dishes',
                    'Afternoon Tea',
                    'Breads',
                    'Salads']

dietTypes = ['everything', 'withoutMeat', 'vegetarian', 'vegan', 'withoutFish', 'withoutDiary']

course_diet = ['Main Dishes_everything',
        'Main Dishes_withoutDiary',
        'Main Dishes_withoutFish',
        'Main Dishes_withoutMeat',
        'Main Dishes_vegetarian',
        'Main Dishes_vegan',
      	'Salads_everything',
        'Salads_withoutDiary',
        'Salads_withoutFish',
        'Salads_withoutMeat',
        'Salads_vegetarian',
        'Salads_vegan']

course_dietType = []
course_dietType_counter = []

for c in courses:
    for dt in dietTypes:
        course_dietType.append(str(c)+'_'+str(dt))



for n in range(1, 10):
    c_d = recipes_data.get('meta0000' + str(n)).get('course_diet').values()
    for cd in c_d:
        course_dietType_counter.append(cd)

for n in range(10, 100):
    c_d = recipes_data.get('meta000' + str(n)).get('course_diet').values()
    for cd in c_d:
        course_dietType_counter.append(cd)

for n in range(100, 1000):
    c_d = recipes_data.get('meta00' + str(n)).get('course_diet').values()
    for cd in c_d:
        course_dietType_counter.append(cd)

for n in range(1000, 10000):
    c_d = recipes_data.get('meta0' + str(n)).get('course_diet').values()
    for cd in c_d:
        course_dietType_counter.append(cd)

for n in range(10000, 27639):
    c_d = recipes_data.get('meta' + str(n)).get('course_diet').values()
    for cd in c_d:
        course_dietType_counter.append(cd)

counter = Counter(course_dietType_counter)

for cour_diet in course_diet:
    print counter.get(cour_diet)
