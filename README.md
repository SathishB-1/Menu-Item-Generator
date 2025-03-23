# 🍽️ Restaurant Name & Menu Generator Using Streamlit & Groq

## 📌 Overview
This project is a **Streamlit-based web application** that generates a **fancy restaurant name** and **menu items** based on a selected cuisine. It uses **LangChain** with the **Groq API (Llama3-8b-8192 model)** to generate names and menu items dynamically.

---

## 📊 Project Workflow

### 1️⃣ Technologies Used
- **Python** (Backend logic)
- **Streamlit** (Web UI)
- **LangChain** (Prompt Engineering)
- **Groq API** (Llama3-8b-8192 Model)
- **Prompt Chaining** (Sequential AI responses)

### 2️⃣ How It Works
1. User selects a **cuisine type** (Indian, Italian, Mexican, etc.).
2. The AI generates a **restaurant name** based on the cuisine.
3. The AI then generates **menu items** based on the restaurant name.
4. The results are displayed on a **Streamlit web app**.

### 3️⃣ Implementation Details
- **Prompt Engineering**: Two separate prompts are used:
  1. Generate a **fancy restaurant name**.
  2. Generate **menu items** based on the restaurant name.
- **LangChain RunnableParallel**: Executes both tasks simultaneously.

---

## 🚀 Code Explanation

### 1️⃣ Import Required Libraries
```python
import os
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.schema.runnable import RunnableParallel, RunnablePassthrough
```

### 2️⃣ Set Up API and Model
```python
# Set Groq Cloud API Key
os.environ["GROQ_API_KEY"] = "your_api_key"



## ⚡ How to Run the Project

1️⃣ Install dependencies:

pip install streamlit langchain langchain_groq

2️⃣ Run the Streamlit app:

streamlit run app.py


## 📌 Future Improvements
   - Add **image generation** for menu items using OpenAI DALL·E.
   - Integrate **real-time restaurant database APIs**.
   - Provide **custom branding suggestions** along with the restaurant name.



