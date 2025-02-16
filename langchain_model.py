import os
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.schema.runnable import RunnableParallel, RunnablePassthrough

# Set Groq Cloud API Key
os.environ["GROQ_API_KEY"] = "your_api_key"

# Initialize the Groq Model
llm = ChatGroq(model_name="llama3-8b-8192", temperature=0.7)


def generate_restaurant_name_and_items(cuisine):
    """Generate a restaurant name and menu items based on the selected cuisine."""
    # Chain 1: Generate a restaurant name
    prompt_template_name = PromptTemplate.from_template(
        "I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
    )

    # Chain 2: Generate menu items based on the restaurant name
    prompt_template_items = PromptTemplate.from_template(
        "Suggest some menu items for {restaurant_name}. Return them as a comma-separated list."
    )

    # Create chains
    name_chain = prompt_template_name | llm
    food_items_chain = prompt_template_items | llm

    # Combine them into a sequence
    chain = RunnableParallel(
        restaurant_name=name_chain,
        menu_items=RunnablePassthrough() | name_chain | food_items_chain,
    )

    # Run the chain
    response = chain.invoke({"cuisine": cuisine})

    # Extract text content from AIMessage objects
    restaurant_name = response['restaurant_name'].content if hasattr(response['restaurant_name'], 'content') else \
    response['restaurant_name']
    menu_items = response['menu_items'].content if hasattr(response['menu_items'], 'content') else response[
        'menu_items']

    return restaurant_name, menu_items


# 🎈 Streamlit UI
st.set_page_config(page_title="Restaurant Name Generator", layout="wide")

st.sidebar.title("🍽️ Select a Cuisine")
cuisine_list = ["Indian", "Italian", "Mexican", "Arabic", "American"]
selected_cuisine = st.sidebar.selectbox("Pick a Cuisine", cuisine_list, index=0)

# Automatically update when cuisine is selected
if selected_cuisine:
    restaurant_name, menu_items_text = generate_restaurant_name_and_items(selected_cuisine)

    # Display Results
    st.title("Menu Item Generator")

    st.subheader(restaurant_name)  # Show restaurant name

    st.subheader("Menu Items")
    menu_items_list = menu_items_text.split(", ")  # Convert to list
    for item in menu_items_list:
        st.write(f"- {item}")  # Display menu items as bullet points
