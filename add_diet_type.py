import pandas as pd
import numpy as np
import json
import itertools

recipes_with_everything = 0
recipes_without_meats = 0
recipes_without_fishes = 0
recipes_without_dairy = 0
recipes_for_vegetarians = 0
recipes_for_vegans = 0

new_recipes_database = {}

recipes_data = json.load(open('recipes.json'))
recipes_ingr_mapped_name = np.load('recipes_ingr_mapped_name_updated.npy')

courses = {'Lunch and Snacks': 'false',
                    'Beverages': 'false',
                    'Breakfast and Brunch': 'false',
                    'Condiments and Sauces': 'false',
                    'Soups': 'false',
                    'Main Dishes': 'false',
                    'Appetizers': 'false',
                    'Cocktails': 'false',
                    'Desserts': 'false',
                    'Side Dishes': 'false',
                    'Afternoon Tea': 'false',
                    'Breads': 'false',
                    'Salads': 'false'}

dietTypes = {'everything': 'false', 'withoutMeat': 'false', 'vegetarian': 'false', 'vegan': 'false', 'withoutFish': 'false', 'withoutDiary': 'false'}

cuisines = {'Swedish': 'false', 'Vietnamese': 'false', 'Kid-Friendly': 'false', 'Cajun & Creole': 'false', 'Indian': 'false', 'Hawaiian': 'false', 'French': 'false', 'Thai': 'false', 'Cuban': 'false',
           'Portuguese': 'false', 'Southwestern': 'false', 'Greek': 'false', 'American': 'false', 'English': 'false', 'Italian': 'false', 'Southern & Soul Food': 'false', 'Irish': 'false',
           'Mexican': 'false', 'Hungarian': 'false', 'Chinese': 'false', 'German': 'false', 'Mediterranean': 'false', 'Japanese': 'false', 'Moroccan': 'false', 'Asian': 'false', 'Spanish': 'false',
           'Barbecue': 'false'}


list_recipes = []
for n in range(1, 10):
    rcp = {}
    rcp['meta0000'+str(n)] = recipes_data.get('meta0000'+str(n))
    crs = rcp.get('meta0000'+str(n)).get('attributes').get('course')
    coursesTemp = courses.copy()
    for cr in crs:
        coursesTemp.update({cr: 'true'})
    rcp.get('meta0000'+str(n))['course'] = coursesTemp
    cui = rcp.get('meta0000'+str(n)).get('attributes').get('cuisine')
    cuisineTemp = cuisines.copy()
    for cu in cui:
        cuisineTemp.update({cu: 'true'})
    rcp.get('meta0000'+str(n))['cuisine'] = cuisineTemp
    del rcp.get('meta0000'+str(n))['attributes']
    list_recipes.append(rcp)

for n in range(10, 100):
    rcp = {}
    rcp['meta000'+str(n)] = recipes_data.get('meta000'+str(n))
    crs = rcp.get('meta000'+str(n)).get('attributes').get('course')
    coursesTemp = courses.copy()
    for cr in crs:
        coursesTemp.update({cr: 'true'})
    rcp.get('meta000'+str(n))['course'] = coursesTemp
    cui = rcp.get('meta000'+str(n)).get('attributes').get('cuisine')
    cuisineTemp = cuisines.copy()
    for cu in cui:
        cuisineTemp.update({cu: 'true'})
    rcp.get('meta000'+str(n))['cuisine'] = cuisineTemp
    del rcp.get('meta000'+str(n))['attributes']
    list_recipes.append(rcp)

for n in range(100, 1000):
    rcp = {}
    rcp['meta00'+str(n)] = recipes_data.get('meta00'+str(n))
    crs = rcp.get('meta00'+str(n)).get('attributes').get('course')
    coursesTemp = courses.copy()
    for cr in crs:
        coursesTemp.update({cr: 'true'})
    rcp.get('meta00'+str(n))['course'] = coursesTemp
    cui = rcp.get('meta00'+str(n)).get('attributes').get('cuisine')
    cuisineTemp = cuisines.copy()
    for cu in cui:
        cuisineTemp.update({cu: 'true'})
    rcp.get('meta00'+str(n))['cuisine'] = cuisineTemp
    del rcp.get('meta00'+str(n))['attributes']
    list_recipes.append(rcp)

for n in range(1000, 10000):
    rcp = {}
    rcp['meta0'+str(n)] = recipes_data.get('meta0'+str(n))
    crs = rcp.get('meta0'+str(n)).get('attributes').get('course')
    coursesTemp = courses.copy()
    for cr in crs:
        coursesTemp.update({cr: 'true'})
    rcp.get('meta0'+str(n))['course'] = coursesTemp
    cui = rcp.get('meta0'+str(n)).get('attributes').get('cuisine')
    cuisineTemp = cuisines.copy()
    for cu in cui:
        cuisineTemp.update({cu: 'true'})
    rcp.get('meta0'+str(n))['cuisine'] = cuisineTemp
    del rcp.get('meta0'+str(n))['attributes']
    list_recipes.append(rcp)

for n in range(10000, 27639):
    rcp = {}
    rcp['meta'+str(n)] = recipes_data.get('meta'+str(n))
    crs = rcp.get('meta'+str(n)).get('attributes').get('course')
    coursesTemp = courses.copy()
    for cr in crs:
        coursesTemp.update({cr: 'true'})
    rcp.get('meta'+str(n))['course'] = coursesTemp
    cui = rcp.get('meta'+str(n)).get('attributes').get('cuisine')
    cuisineTemp = cuisines.copy()
    for cu in cui:
        cuisineTemp.update({cu: 'true'})
    rcp.get('meta'+str(n))['cuisine'] = cuisineTemp
    del rcp.get('meta'+str(n))['attributes']
    list_recipes.append(rcp)

meats = ["bacon", "smoked_sausage", "smoked_summer_sausage", "meat", "smoked_pork", "raw_pork", "ham", "beef",
         "roasted_beef", "guineafowl", "fried_chicken", "grilled_beef", "red_meat", "fried_pork", "pork", "frankfurter",
         "raw_chicken", "boiled_chicken", "beef_broth", "uncured_boiled_pork", "boiled_meat", "uncured_smoked_pork",
         "seal", "mutton", "roasted_meat", "turkey", "boiled_beef", "veal", "chicken_liver", "raw_lamb",
         "roasted_turkey", "pickled_ham", "roasted_lamb", "raw_beef", "mutton_liver", "chicken_broth",
         "smoked_pork_belly", "fried_beef", "liver", "ewe", "fried_cured_pork", "roasted_pork", "boiled_pork",
         "beef_tallow", "beef_liver", "cured_ham", "lamb_liver", "lamb", "pork_sausage", "grilled_pork", "uncured_pork",
         "chicken", "raw_turkey", "cured_pork", "pork_liver", "roasted_chicken", "boiled_mutton", "nezara_viridula",
         "musk", "honey", "castoreum", "cod_liver_oil", "chrysocoris_stolli", "gelatin", "auto_oxidized_salmon_oil",
         "fish_oil", "egg", "cockroach", "silk_fibrooin", "feces", "lard", "animal", "bone_oil", "silkworm_chrysalis",
         "oxidized_lard"]

fishes = ["mackerel", "keta_salmon", "dolphin", "trassi", "prawn", "salmon_caviar", "shellfish", "whitefish", "cod",
          "sweetfish", "tuna", "boiled_crab", "eel", "octopus", "mantis_shrimp", "raw_lean_", "fish", "catfish",
          "salmon_roe", "clam", "lobster", "smoked_herring", "shrimp", "globefish", "japanese_seafood", "herring",
          "lean_fish", "krill", "katsuobushi", "smoked_fish", "fish", "haddock", "salmon", "oyster", "sperm_whale_oil",
          "scallop", "fermented_shrimp", "smoked_fatty_fish", "crayfish", "roasted_shrimp", "pilchard",
          "horse_mackerel", "smoked_salmon", "cuttlefish", "mussel", "crab", "raw_fish", "fatty_fish", "salmon_oil",
          "seaweed", "sea_bass", "squid", "whale", "raw_fatty_fish", "pike", "caviar", "sturgeon_caviar"]

dairy = ["cottage_cheese", "cheddar_cheese", "tilsit_cheese", "goat_cheese", "milk_fat", "sour_milk", "sheep_cheese",
         "goat_milk", "yogurt", "sheep_milk", "butter", "milk", "camembert_cheese", "oxidized_milk", "butterfat",
         "limburger_cheese", "cheese", "domiati_cheese", "comte_cheese", "swiss_cheese", "cream", "butter_oil",
         "parmesan", "dairy", "roquefort_cheese", "skim_milk", "gruyere_cheese", "blue_cheese", "provolone_cheese",
         "buttermilk", "oxidized_skim_milk", "cream_cheese", "emmental_cheese", "russian_cheese", "mozzarella_cheese",
         "romano_cheese", "parmesan_cheese", "feta_cheese", "munster_cheese"]

meats_set = set(meats)
fishes_set = set(fishes)
dairy_set = set(dairy)

idx = 0
for rec, rec_ingr in itertools.izip(list_recipes, recipes_ingr_mapped_name):

    idx += 1

    if (idx > 0 and idx < 10):
        id = 'meta0000' + str(idx)

    if (idx >= 10 and idx < 100):
        id = 'meta000' + str(idx)

    if (idx >= 100 and idx < 1000):
        id = 'meta00' + str(idx)

    if (idx >= 1000 and idx < 10000):
        id = 'meta0' + str(idx)

    if (idx >= 10000 and idx < 27639):
        id = 'meta' + str(idx)

    dietTypesTemp = dietTypes.copy()
    rec.get(id)['dietType'] = dietTypesTemp
    rec.get(id).get('dietType')['everything'] = 'true'
    new_recipes_database.update(rec)
    recipes_with_everything += 1

    temp2 = set(rec_ingr)
    meat_inter = temp2.intersection(meats_set)
    fish_inter = temp2.intersection(fishes_set)
    dairy_inter = temp2.intersection(dairy_set)

    if not meat_inter:
        rec.get(id).get('dietType')['withoutMeat'] = 'true'
        recipes_without_meats += 1

        if not fish_inter:
            rec.get(id).get('dietType')['vegetarian'] = 'true'
            recipes_for_vegetarians += 1

            if not dairy_inter:

                rec.get(id).get('dietType')['vegan'] = 'true'
                recipes_for_vegans += 1

    if not fish_inter:
        rec.get(id).get('dietType')['withoutFish'] = 'true'
        recipes_without_fishes += 1

    if not dairy_inter:
        rec.get(id).get('dietType')['withoutDiary'] = 'true'
        recipes_without_dairy += 1

print 'Recipes with everything', recipes_with_everything
print 'Recipes without meat', recipes_without_meats
print 'Recipes without fishes', recipes_without_fishes
print 'Recipes without diary', recipes_without_dairy
print 'Recipes for vegetarians', recipes_for_vegetarians
print 'Recipes for vegans', recipes_for_vegans

with open('recipes_withDishType_withoutParent_prepared4filtr.json', 'w') as outfile:
    json.dump(new_recipes_database, outfile)