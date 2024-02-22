import json
from recipe import Recipe
from menu import Menu

# Global variables
recipes = []
menus = []
current_user = None  # Placeholder for user authentication

# Functions for Recipe Management

def add_recipe():
    global recipes, current_user
    # Get input for recipe attributes
    name = input("Enter recipe name: ")
    ingredients = input("Enter ingredients (comma-separated): ").split(',')
    instructions = input("Enter instructions: ")
    category = input("Enter category: ")
    preparation_time = input("Enter preparation time: ")
    difficulty_level = input("Enter difficulty level: ")
    tags = input("Enter tags (comma-separated): ").split(',')
    cuisine = input("Enter cuisine type: ")
    notes = input("Enter notes: ")
    image_url = input("Enter image URL: ")
    chef = current_user  # Assuming the current user is the chef creating the recipe
    new_recipe = Recipe(name, ingredients, instructions, category, preparation_time, difficulty_level, tags, cuisine, notes, image_url, chef)
    recipes.append(new_recipe)
    print("Recipe added successfully!")

def edit_recipe():
    global recipes
    recipe_name = input("Enter the name of the recipe you want to edit: ")
    for recipe in recipes:
        if recipe.name.lower() == recipe_name.lower():
            print("Enter new details:")
            recipe.name = input("Enter recipe name: ")
            recipe.ingredients = input("Enter ingredients (comma-separated): ").split(',')
            recipe.instructions = input("Enter instructions: ")
            recipe.category = input("Enter category: ")
            recipe.preparation_time = input("Enter preparation time: ")
            recipe.difficulty_level = input("Enter difficulty level: ")
            recipe.tags = input("Enter tags (comma-separated): ").split(',')
            recipe.cuisine = input("Enter cuisine type: ")
            recipe.notes = input("Enter notes: ")
            recipe.image_url = input("Enter image URL: ")
            print("Recipe edited successfully!")
            return
    print("Recipe not found.")

def delete_recipe():
    global recipes
    recipe_name = input("Enter the name of the recipe you want to delete: ")
    for recipe in recipes:
        if recipe.name.lower() == recipe_name.lower():
            recipes.remove(recipe)
            print("Recipe deleted successfully!")
            return
    print("Recipe not found.")

def display_recipe(recipe):
    recipe.display_recipe_details()

# Functions for Menu Management

def create_menu():
    global menus
    name = input("Enter menu name: ")
    description = input("Enter menu description: ")
    new_menu = Menu(name, description)
    
    while True:
        recipe_name = input("Enter recipe name to add to this menu (or leave blank to finish): ")
        if not recipe_name:
            break
        found = False
        for recipe in recipes:
            if recipe.name.lower() == recipe_name.lower():
                new_menu.add_recipe(recipe)
                found = True
                break
        if not found:
            print("Recipe not found.")
    
    menus.append(new_menu)
    print("Menu created successfully!")

def edit_menu():
    global menus
    menu_name = input("Enter the name of the menu you want to edit: ")
    for menu in menus:
        if menu.name.lower() == menu_name.lower():
            print("Edit menu options:")
            print("1. Add Recipe")
            print("2. Remove Recipe")
            print("3. Edit Description")
            print("4. Cancel")
            edit_choice = input("Enter your choice: ")
            if edit_choice == '1':
                recipe_name = input("Enter recipe name to add to this menu: ")
                for recipe in recipes:
                    if recipe.name.lower() == recipe_name.lower():
                        menu.add_recipe(recipe)
                        print("Recipe added to menu.")
                        break
                else:
                    print("Recipe not found.")
            elif edit_choice == '2':
                recipe_name = input("Enter recipe name to remove from this menu: ")
                for recipe in menu.recipes:
                    if recipe.name.lower() == recipe_name.lower():
                        menu.remove_recipe(recipe)
                        print("Recipe removed from menu.")
                        break
                else:
                    print("Recipe not found in this menu.")
            elif edit_choice == '3':
                new_description = input("Enter new menu description: ")
                menu.description = new_description
                print("Menu description updated.")
            elif edit_choice == '4':
                print("Menu edit cancelled.")
            else:
                print("Invalid choice.")
            return
    print("Menu not found.")

def delete_menu():
    global menus
    menu_name = input("Enter the name of the menu you want to delete: ")
    for menu in menus:
        if menu.name.lower() == menu_name.lower():
            menus.remove(menu)
            print("Menu deleted successfully!")
            return
    print("Menu not found.")

def display_menu(menu):
    menu.display_menu_details()

# Main Function

def main():
    global current_user, recipes, menus
    # Load recipes and menus for the current user (Placeholder)
    # load_data_for_current_user()

    while True:
        print("\nRecipe Management System")
        print("1. Add Recipe")
        print("2. Edit Recipe")
        print("3. Delete Recipe")
        print("4. View Recipes")
        print("5. Create Menu")
        print("6. Edit Menu")
        print("7. Delete Menu")
        print("8. View Menus")
        print("9. Search Recipes/Menus")
        print("10. Import Recipes")
        print("11. Export Recipes")
        print("12. User Settings")
        print("13. Logout")
        print("14. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_recipe()
        elif choice == '2':
            edit_recipe()
        elif choice == '3':
            delete_recipe()
        elif choice == '4':
            for recipe in recipes:
                display_recipe(recipe)
        elif choice == '5':
            create_menu()
        elif choice == '6':
            edit_menu()
        elif choice == '7':
            delete_menu()
        elif choice == '8':
            for menu in menus:
                display_menu(menu)
        elif choice == '9':
            # Add functionality for search
            pass
        elif choice == '10':
            # Add functionality for importing recipes
            pass
        elif choice == '11':
            # Add functionality for exporting recipes
            pass
        elif choice == '12':
            # Add functionality for user settings
            pass
        elif choice == '13':
            # Add functionality for logout
            pass
        elif choice == '14':
            print("Exiting...")
            break  # Exit the while loop and end the program
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

