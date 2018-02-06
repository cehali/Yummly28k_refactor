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
    rcp = recipes_data.get('meta0000'+str(n))
    rcp['key'] = 'meta0000'+str(n)
    list_recipes.append(rcp)

for n in range(10, 100):
    rcp = recipes_data.get('meta000'+str(n))
    rcp['key'] = 'meta000'+str(n)
    list_recipes.append(rcp)

for n in range(100, 1000):
    rcp = recipes_data.get('meta00'+str(n))
    rcp['key'] = 'meta00'+str(n)
    list_recipes.append(rcp)

for n in range(1000, 10000):
    rcp = recipes_data.get('meta0'+str(n))
    rcp['key'] = 'meta0'+str(n)
    list_recipes.append(rcp)

for n in range(10000, 27639):
    rcp = recipes_data.get('meta'+str(n))
    rcp['key'] = 'meta'+str(n)
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
recipes_list_2json = []
for rec, rec_ingr in itertools.izip(list_recipes, recipes_ingr_mapped_name):
    idx += 1

    rec['dietType'] = ['everything']

    temp2 = set(rec_ingr)
    meat_inter = temp2.intersection(meats_set)
    fish_inter = temp2.intersection(fishes_set)
    dairy_inter = temp2.intersection(dairy_set)

    if not meat_inter:
        rec['dietType'].append('withoutMeat')

        if not fish_inter:
            rec['dietType'].append('vegetarian')

            if not dairy_inter:
                rec['dietType'].append('vegan')

    if not fish_inter:
        rec['dietType'].append('withoutFish')

    if not dairy_inter:
        rec['dietType'].append('withoutDiary')

    recipes_list_2json.append(rec)


new_recipes_database.update(recipes_list_2json)
with open('yummmly_recipes.json', 'w') as outfile:
        json.dump(new_recipes_database, outfile)