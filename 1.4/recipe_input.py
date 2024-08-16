import pickle

def calc_difficulty(cooking_time,ingredients):
    for recipe in recipes_list:
        if cooking_time < 10 and ingredients < 4:
            return "Easy"
        elif cooking_time < 10 and ingredients >= 4:
            return "Medium"
        elif cooking_time >= 10 and ingredients < 4:
            return "Interm."
        elif cooking_time >= 10 and ingredients >= 4:
            return "Hard"

def take_recipe():
    name = str(input('Enter the name of a recipe: '))
    cooking_time = int(input('Enter how long it takes to make the recipe in minutes: '))
    ingredients = list(input("Enter the ingredients in the recipe: ").split(","))
    recipe ={
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients
    }
    difficulty = calc_difficulty(cooking_time,len(ingredients))
    return {"name" : name, "cooking time": cooking_time, "ingredients": ingredients, "difficulty": difficulty}


recipe_file = input("Enter the name of the file: ")
try:
    with open(recipe_file,'rb') as file:
        data = pickle.load(file)
except FileNotFoundError:
    data = {"recipes_list": [], "ingredients_list": []}
except Exception as e:
    print("something went wrong :(")

recipes_list, ingredients_list = data["recipes_list"], data["ingredients_list"]

n = int(input("How many recipes would you like to add: "))

for i in range(n):
    recipe = take_recipe()
    for ingredient in recipe['ingredients']:
        if not ingredient in ingredients_list:
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)

data = {"recipes_list" : recipes_list, "ingredients_list": ingredients_list}
with open(recipe_file, "wb") as file:
    pickle.dump(data, file)