# Automated Recipe Generator

## Overview
The **Automated Recipe Generator** is a web-based application built using **Streamlit** and the **Spoonacular API**. Users can enter a list of ingredients, and the app generates recipes that use those ingredients. The application provides details such as:
- Recipe names
- Recipe images
- Used and missing ingredients
- Full ingredient list
- Step-by-step cooking instructions

---

## Features
1. **Ingredient-Based Recipe Search:**
   - Users input a comma-separated list of ingredients.
   - The app fetches recipes using those ingredients from the Spoonacular API.

2. **Recipe Details Display:**
   - Displays the recipe title and image.
   - Lists used and missing ingredients.
   - Provides a complete ingredient list.
   - Displays step-by-step cooking instructions.

3. **Error Handling:**
   - Handles API errors and provides user-friendly messages.

---

## Technologies Used
- **Python**: Core programming language for backend logic.
- **Streamlit**: Web framework to create an interactive user interface.
- **Spoonacular API**: External API to fetch recipes and their details.
- **BeautifulSoup**: Used to clean up and format the instructions provided by the API.
- **Requests**: For making HTTP requests to the Spoonacular API.

---

## Dependencies
To run this project, ensure you have the following Python packages installed:
```bash
pip install streamlit requests beautifulsoup4
```

---

## Installation & Setup
### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/recipe-generator.git
cd recipe-generator
```

### Step 2: Set Up API Key
- Get a **Spoonacular API Key** from [Spoonacular](https://spoonacular.com/food-api).
- Replace `API_KEY` in **app.py** with your own API key.

### Step 3: Run the Application
```bash
streamlit run app.py
```

---

## File Structure
```
recipe-generator/
├── api/
│   └── spoonacular.py  # Handles API requests to Spoonacular
├── utils/
│   └── helpers.py      # Utility functions for formatting recipes
├── app.py              # Main Streamlit application
├── README.txt          # Documentation
└── requirements.txt    # List of dependencies
```

---

## How It Works
1. The user enters a list of ingredients.
2. The app fetches matching recipes from the **Spoonacular API**.
3. It displays:
   - Recipe names and images
   - Used and missing ingredients
   - Full ingredient list
   - Step-by-step instructions
4. Recipes are formatted using **BeautifulSoup** for better readability.

---

## Potential Improvements
- Add **meal planning features**.
- Allow users to **save favorite recipes**.
- Integrate **nutritional information** for each recipe.
- Provide a **filter option** for dietary preferences (vegan, gluten-free, etc.).

---

## Contact
For any queries, contact:
- **Email**: your-email@example.com
- **GitHub**: [your-username](https://github.com/your-username)

Happy Cooking! 🍳

