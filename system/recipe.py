# recipe.py

class Recipe:
    def __init__(self, name, ingredients, instructions, category, preparation_time, difficulty_level, tags, cuisine, notes, image_url, chef):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.category = category
        self.preparation_time = preparation_time
        self.difficulty_level = difficulty_level
        self.tags = tags
        self.cuisine = cuisine
        self.notes = notes
        self.image_url = image_url
        self.chef = chef

    def __str__(self):
        return f"{self.name} - {self.category} - Time: {self.preparation_time} - Difficulty: {self.difficulty_level} - Cuisine: {self.cuisine}"

    def display_recipe_details(self):
        print(f"\nName: {self.name}")
        print(f"Category: {self.category}")
        print(f"Preparation Time: {self.preparation_time}")
        print(f"Difficulty Level: {self.difficulty_level}")
        print(f"Cuisine: {self.cuisine}")
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")
        print("Instructions:")
        print(self.instructions)
        print("Tags:", ', '.join(self.tags))
        print("Notes:", self.notes)
        print("Image URL:", self.image_url)
        print("Chef:", self.chef)

