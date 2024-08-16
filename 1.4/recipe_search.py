import pickle

def display_recipe(recipe):
    print("Recipe: " , recipe["name"])
    print("Cooking Time: " , recipe["cooking time"] )
    print("Ingedients: ")
    for ingredient in recipe["ingredients"]:
        print(ingredient)
    print("Difficulty :", recipe["difficulty"])

def search_ingredients(data):
    all_ingredients = data["ingredients_list"]
    for i, ingredient in enumerate(all_ingredients):
        print(f"{i+1}.) {ingredient.title()}")
    try:
        while True:
            selection = int(input("Enter the index of an ingredient you wan: "))
            if 1 <= selection <= len(all_ingredients):
                ingredient_searched = all_ingredients[selection-1]
                break
            print("enter a valid number")
        recipes_with_ingredient = [recipe for recipe in data["recipes_list"] if ingredient_searched in recipe["ingredients"]]
        num_recipes = len(recipes_with_ingredient)
        recipe_word = "Recipe" if num_recipes == 1 else "Recipes"
        for recipe in recipes_with_ingredient:
            display_recipe(recipe)
    except ValueError:
            print("something went wrong")
    except IndexError:
        print("something went wrong")

recipe_file = input("Enter the name of the file: ")

try:
    with open(recipe_file, "rb") as file:
        data = pickle.load(file)
except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
else:
    search_ingredients(data)