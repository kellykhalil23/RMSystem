# menu.py
class Menu:
    def __init__(self, name, description, recipes=None):
        self.name = name
        self.description = description
        self.recipes = recipes if recipes else []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def remove_recipe(self, recipe):
        if recipe in self.recipes:
            self.recipes.remove(recipe)

    def display_menu_details(self):
        print(f"\nMenu: {self.name}")
        print(f"Description: {self.description}")
        print("Recipes:")
        for recipe in self.recipes:
            print(f"- {recipe.name}")
