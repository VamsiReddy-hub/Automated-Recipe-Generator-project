# app.py
import os
import streamlit as st

from api.spoonacular import SpoonacularAPI
from utils.helpers import format_recipe

# Read the key from an environment variable
API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    st.error(
        "❌  API_KEY environment variable not set.\n\n"
        "• In local dev, create a .env file (API_KEY=your‑key) and run `streamlit run app.py`.\n"
        "• On Render, add the variable in **Dashboard → Environment → Add Variable**."
    )
    st.stop()

spoonacular = SpoonacularAPI(API_KEY)

st.title("Automated Recipe Generator")

ingredients = st.text_input("Enter ingredients (comma‑separated):")
number_of_recipes = st.number_input(
    "Number of recipes to generate:", min_value=1, max_value=10, value=5
)

if st.button("Generate Recipes"):
    if not ingredients:
        st.warning("Please enter some ingredients.")
        st.stop()

    try:
        recipes = spoonacular.search_recipes_by_ingredients(
            ingredients, number=number_of_recipes
        )

        for recipe in recipes:
            st.subheader(recipe["title"])
            st.image(recipe["image"])

            st.write("**Used Ingredients:**")
            st.write(", ".join(i["name"] for i in recipe["usedIngredients"]))

            st.write("**Missing Ingredients:**")
            st.write(", ".join(i["name"] for i in recipe["missedIngredients"]))

            details = spoonacular.get_recipe_details(recipe["id"])

            st.write("**Full Ingredients List:**")
            st.write(", ".join(i["name"] for i in details["extendedIngredients"]))

            st.write("**Instructions:**")
            st.write(format_recipe(details))
            st.markdown("---")

    except Exception as e:
        st.error(f"Error: {e}")
