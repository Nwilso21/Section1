recipes_list = []
ingredients_list = []

def take_recipe():
    name = str(input('Enter the name of a recipe: '))
    cooking_time = int(input('Enter how long it takes to make the recipe in minutes: '))
    ingredients = list(input("Enter the ingredients in the recipe: ").split(","))
    recipe ={
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients
    }
    return recipe

n = int(input("How many recipes would you like to add: "))

for i in range(n):
    recipe = take_recipe()
    for ingredient in recipe['ingredients']:
        if not ingredient in ingredients_list:
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)

for recipe in recipes_list:
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
        recipe['difficulty'] = "Easy"
    elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
        recipe['difficulty'] = "Medium"
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
        recipe['difficulty'] = "Intermediate"
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
        recipe['difficulty'] = "Hard"


for recipe in recipes_list:
    print("Recipe: " , recipe["name"])
    print("Cooking Time: " , recipe["cooking_time"] )
    print("Ingedients: ")
    for ingredient in recipe["ingredients"]:
        print(ingredient)
    print("Difficulty :", recipe["difficulty"])

ingredients_list.sort()
print("Ingredients Available Across All Recipes")
print("-------------------------------------------")
for ingredient in ingredients_list:
    print(ingredient)
