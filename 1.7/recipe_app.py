from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker



engine = create_engine("mysql://cf-python:password@localhost/task_database2")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Recipe(Base):
    __tablename__ = "final_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + ">"

    def __str__(self):
        print(self.name, ": \n")
        print("\t Ingredients: ", self.ingredients)
        print("\t Time to Cook: ", self.cooking_time)
        print("\t Difficulty : ", self.difficulty)

    def calculateDifficulty(self,):
        if int(self.cooking_time) < 10 and len(self.ingredients) < 4:
            self.difficulty = 'Easy'
        elif int(self.cooking_time) < 10 and len(self.ingredients) >= 4:
             self.difficulty = 'Medium'
        elif int(self.cooking_time) >= 10 and len(self.ingredients) < 4:
            self.difficulty = 'intermediate'
        elif int(self.cooking_time) >= 10 and len(self.ingredients) >= 4:
            self.difficulty = 'Hard'

    def return_ingredients_as_list(self):
        new_ingredients = set()
        if self.ingredients == '':
            new_ingredients =[]
            return new_ingredients
        else:
            new_ingredients = self.ingredients.split(',')

Base.metadata.create_all(engine)


def create_Recipe():
    name_Check = 0
    time_Check = 0
    while name_Check != 1:
        name = input("Enter the name of the recipe: ")
        if len(name) <= 50:
            name_Check = 1

    while time_Check != 1:
        cooking_time = input("Enter how long it takes to cook: ")
        if cooking_time.isnumeric() == True:
            time_Check = 1


    ingredients_loop_control = input("Enter how many ingredients you would like to add: ")
    temp_ingredients = []
    for x in range(int(ingredients_loop_control)):
        current_ingredient = input("Enter an ingredient: ")
        temp_ingredients.append(current_ingredient)
    new_ingredients_list = ','.join(temp_ingredients)

    recipe_entry = Recipe(name=name,ingredients=new_ingredients_list,cooking_time=cooking_time)
    recipe_entry.calculateDifficulty()
    session.add(recipe_entry)
    session.commit()
    print("Recipe Added \n")



def view_all_recipes():
    recipes = session.query(Recipe).all()
    
    if recipes :
        for recipe in recipes:
            print(recipe.__str__())
    else :
        print("There are no Recipes :(")
        return None



def search_by_ingredients():
    if session.query(Recipe).count() == 0 :
        print("There are no Recipes :(")
        return None
    else :
        results = session.query(Recipe.ingredients).all()
        all_ingredients =[]
        all_ingredients2 =[]
        new_ingredients =[]
        for result in results:
            new_ingredients.append(result[0].split(','))
        for ingredient in new_ingredients:
            range = len(ingredient)
            count = 0
            while count < range:
                all_ingredients2.append(ingredient[count].split(','))
                count +=1
        for ingredient in all_ingredients2:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)
        print("Ingredients : \n")
        for idx, ingredient in enumerate(all_ingredients, start=1):
            print(f"{idx}. {ingredient}")
        searched = input("What ingredients would you like to search for (Enter the IDs separated by spaces) : ").split(' ')
        search_Ingredients = [all_ingredients[int(id) - 1] for id in searched]
        conditions = []
        for ingredient in search_Ingredients:
            conditions.append(ingredient[0])
        results =[]
        for condition in conditions:
            results.append(session.query(Recipe).filter(Recipe.ingredients.like(f"%{condition}%")).all())
        if results == '':
            print("There are no recipes with that ingrdient :(")
        else:
            for result in results:
                print(result.__str__())



def edit_recipe():
    if session.query(Recipe).count() == 0 :
        print("There are no Recipes :(")
        return None
    else :
        results = session.query(Recipe.id,Recipe.name).all()
        for result in results:
            print(result[0],result[1])

        selected = int(input("Enter the ID of the recipe you want to change: "))
        recipe_to_edit = session.query(Recipe).filter(Recipe.id==selected).first()
        if not recipe_to_edit:
            print("That recipe does not exist :(")
            return None
        else:
            print("1. ", recipe_to_edit.name)
            print("2. ", recipe_to_edit.cooking_time)
            print("3. ", recipe_to_edit.ingredients)
            update_selection = int(input("What do you wish to change (Enter the ID): "))
            if update_selection == 1:
                name_Check = 0
                while name_Check == 0:
                    changed_name = input("Enter the new name of the recipe: ")
                    if len(changed_name) <= 50:
                        name_Check = 1
                recipe_to_edit.name = changed_name
            elif update_selection == 2:
                time_Check = 0
                while time_Check == 0:
                    changed_time = input("Enter the new cook time of the recipe: ")
                    if changed_time.isnumeric() == True:
                        time_Check = 1
                recipe_to_edit.cooking_time = changed_time
            elif update_selection == 3:
                ingredients_loop_control = input("Enter how many ingredients you would like to add: ")
                temp_ingredients = []
                for x in range(int(ingredients_loop_control)):
                    current_ingredient = input("Enter an ingredient: ")
                    temp_ingredients.append(current_ingredient)
                recipe_to_edit.ingredients = ','.join(temp_ingredients)
            recipe_to_edit.calculateDifficulty()
            session.commit()
            print("Recipe Changed :)")

def delete_recipe():
    if session.query(Recipe).count() == 0 :
        print("There are no Recipes :(")
        return None
    else :
        results = session.query(Recipe.id,Recipe.name).all()
        for result in results:
            print(result[0],result[1])

        selected = int(input("Enter the ID of the recipe you want to delete: "))
        recipe_to_delete = session.query(Recipe).filter(Recipe.id==selected).first()
        decision = input("Are you sure you want to delete that one: ")
        if decision == 'yes':
            session.delete(recipe_to_delete)
        else:
            print ("No recipes changed")
            return None


running = 0
while running == 0:
    print("--------------Recipes Function---------------")
    print("--Make a choice from the following options---")
    print("---------1) Create A New Recipe--------------")
    print("---------2) View all Recipes-----------------")
    print("---------3) Search an Ingredient-------------")
    print("---------4) Edit a Recipe -------------------")
    print("---------5) Delete a Recipe -----------------")
    print("---------Type quit to exit ------------------")
    print("\n")
    print("\n")
    choice = input("Enter the number of the option you want:  ")
    if choice == '1':
        create_Recipe()
    elif choice == '2':
        view_all_recipes()
    elif choice == '3':
        search_by_ingredients()
    elif choice == '4':
        edit_recipe()
    elif choice == '5':
        delete_recipe()
    elif choice == 'quit':
        running =1
    else :
        print("That is not an option :(")

