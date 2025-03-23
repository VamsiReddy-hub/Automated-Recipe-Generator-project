import streamlit as st
from api.spoonacular import SpoonacularAPI
from utils.helpers import format_recipe


API_KEY = "4bcaafd23e0442a2a27b95a6189ac235"  # Your Spoonacular API key
spoonacular = SpoonacularAPI(API_KEY)


st.title("Automated Recipe Generator")


ingredients = st.text_input("Enter ingredients (comma-separated):")
number_of_recipes = st.number_input("Number of recipes to generate:", min_value=1, max_value=10, value=5)

if st.button("Generate Recipes"):
    if ingredients:
        try:
         
            recipes = spoonacular.search_recipes_by_ingredients(ingredients, number=number_of_recipes)
            

            for recipe in recipes:
                st.subheader(recipe['title'])
                st.image(recipe['image'])
                
                st.write("Used Ingredients:")
                st.write(", ".join([ingredient['name'] for ingredient in recipe['usedIngredients']]))
                
                st.write("Missing Ingredients:")
                st.write(", ".join([ingredient['name'] for ingredient in recipe['missedIngredients']]))
                
                details = spoonacular.get_recipe_details(recipe['id'])
                
                st.write("Full Ingredients List:")
                st.write(", ".join([ingredient['name'] for ingredient in details['extendedIngredients']]))
                
                st.write("Instructions:")
                st.write(format_recipe(details))  
                st.write("------")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter some ingredients.")
