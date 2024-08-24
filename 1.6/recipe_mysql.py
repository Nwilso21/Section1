import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password')

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS task_database2")
cursor.execute("USE task_database2")
cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(
    id             INT AUTO_INCREMENT PRIMARY KEY,
    name           VARCHAR(50),
    ingredients    VARCHAR(255),
    cooking_time   INT,
    difficulty     VARCHAR(20)             
)''')

def fix(ingredients):
     return ', '.join([ingredient.strip() for ingredient in ingredients.split(',')])

def calculateDifficulty(cooking_time,ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
       return "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
         return "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        return "Interm."
    elif cooking_time >= 10 and len(ingredients) >= 4:
        return "Hard"

def createRecipe():
    name = str(input("Enter the name of the recipe: "))
    cooking_time = int(input("Enter how long it takes to cook: "))
    ingredients = input("Enter the ingredients in the recipe: ")
    difficulty=calculateDifficulty(cooking_time,ingredients)
    newIngredients=fix(ingredients)
    try:
            insert_query = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_query, (name, newIngredients, cooking_time, difficulty))
            conn.commit()

            print("  ** Recipe successfully added! **")
    except mysql.connector.Error as err:
            print("Error occurred: ", err)


def ingSearch():
    cursor.execute("SELECT DISTINCT ingredients FROM Recipes")
    results = cursor.fetchall()
    allIngredients = set()
    for result in results:
        ingredients = result[0].split(",")
        for ingredient in ingredients:
            allIngredients.add(ingredient.strip())

    for idx, ingredient in enumerate(sorted(allIngredients), start=1):
        print(f"{idx}. {ingredient}")

    choice = int(input("Choose an ingredient to search by ID: ")) -1
    searched= sorted(allIngredients)[choice]

    cursor.execute("SELECT * FROM Recipes WHERE ingredients LIKE %s", ('%' + searched+ '%',))

    results = cursor.fetchall()
    if results:
        for result in results:
            print(result)
    else:
        print("Something went wrong")

def recipeUpdate():
    cursor.execute("SELECT id, name FROM Recipes")
    recipes = cursor.fetchall()
    for recipe in recipes:
        print(f"ID: {recipe[0]}, Name: {recipe[1]}")
    selected = int(input("Enter which recipe you would like to change: "))
    selected2 = input("What do you want to change: ")

    if selected2 == 'name':
        newName = input("Enter the new name of the recipe: ")
        cursor.execute("UPDATE Recipes SET name = %s WHERE id = %s", (newName,selected))
    elif selected2 == 'ingredients':
        ings = input("Enter the new ingredients: ")
        fixed=fix(ings)
        cursor.execute("UPDATE Recipes SET ingredients =%s WHERE id = %s", (fixed,selected))
    elif selected2 == 'cooking_time':
        newTime = int(input('Enter the new cook time: '))
        cursor.execute("UPDATE Recipes SET cooking_time = %s WHERE id = %s", (newTime,selected))

    cursor.execute("SELECT cooking_time, ingredients FROM Recipes WHERE id = %s", (selected,))
    recipe = cursor.fetchone()
    newDiff=calculateDifficulty(recipe[0],recipe[1])
    cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s", (newDiff, selected))
def recipeDelete():
    cursor.execute("SELECT id, name FROM Recipes")
    recipes = cursor.fetchall()
    for recipe in recipes:
        print(f"ID: {recipe[0]}, Name: {recipe[1]}")
    selected = int(input("Enter which recipe you would like to remove: "))
    cursor.execute("DELETE FROM Recipes WHERE id = %s", (selected,))
    



choice = ''
while(choice != 'quit'):
    print("Pick a choice")
    print("          1.Create a new recipe")
    print("          2.Search for a recipe by ingredient")
    print("          3.Update an existing recipe")
    print("          4.Delete a recipe")
    print("          Type 'quit' to exit the program")
    choice = input("Your choice: ")

    if choice == '1':
        createRecipe()
        conn.commit()
    elif choice =='2':
        ingSearch()
        conn.commit()
    elif choice =='3':
        recipeUpdate()
        conn.commit()
    elif choice =='4':
        recipeDelete()
        conn.commit()