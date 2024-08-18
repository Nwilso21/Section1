class Recipe(object):
    
    all_ingredients =set()

    def __init__(self,name,ingredients,cooking_time):
        self.name = name
        self.ingredients = ingredients
        self.cooking_time = cooking_time
        self.difficulty = self.calculateDifficulty

    def setName(self):
        self.name = str(input("Enter the name of the recipe: "))

    def getName(self):
        output = str(self.name)
        return output
    
    def setCookingTime(self):
        self.cooking_time = int(input("Enter how long it takes to cook: "))
        
    def getCookingTime(self):
        output = int(self.cooking_time)
        return output

    def addIngredients(self, ingList):
        for ing in ingList:
            self.ingredients.append(ingredient)

    def getIngredient(self):
        for ingredient in self.ingredients:
            output = str(ingredient)
            return output

    def calculateDifficulty(self):
        if self.cooking_time < 10 and len(self.ingredients) < 4:
            self.difficulty = str("Easy")
        elif self.cooking_time < 10 and len(self.ingredients) >= 4:
            self.difficulty = str("Medium")
        elif self.cooking_time >= 10 and len(self.ingredients) < 4:
            self.difficulty = str("Intermediate")
        elif self.cooking_time >= 10 and len(self.ingredients) >= 4:
           self.difficulty = str("Hard")

    def getDifficulty(self):
        if self.difficulty is None:
            self.calculateDifficulty()
        return self.difficulty

    def searchIngredient(self, searched):
        isFound = 0
        for ingredient in self.ingredients:
            if searched.lower() == ingredient.lower():
                isFound= 1
        return bool(isFound)

    def updateAllIngredients(self):
        for ingredient in self.ingredients:
            if not ingredient in all_ingredients:
                all_ingredients.append(ingredient)
        recipes_list.append(recipe)

def recipeSearch(data, searchTerm):
    print("The recipes containing: ", searchTerm,  "are : ")
    for recipe in data:
        if recipe.searchIngredient(searchTerm):
            print(recipe.getName())
            
tea = Recipe("Tea", ["Tea Leaves", "Sugar", "Water"], 5)
coffee = Recipe("Coffee", ["Coffee Powder", "Sugar", "Water"], 5)
cake = Recipe("Cake", ["Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk"], 50)
smoothie = Recipe("Banana Smoothie", ["Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes"], 5)

# Add recipes to a list
recipes_list = [tea, coffee, cake, smoothie]
for recipe in recipes_list:
    print(recipe.getName())
recipeSearch(recipes_list,"Water")