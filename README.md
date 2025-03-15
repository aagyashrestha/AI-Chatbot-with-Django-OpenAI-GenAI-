AI Chatbot with Django & OpenAI (GenAI)

This project is a Generative AI (GenAI) chatbot built using Django and the OpenAI API. It allows users to interact with an AI-powered chatbot that responds to user input with context-based replies. The chatbot stores conversation history and maintains context throughout the session, leveraging OpenAI's GPT-3.5 model for generating dynamic, human-like responses.
Features

Generative AI (GenAI) powered chatbot using OpenAI's GPT-3.5 model.
Basic chat functionality using the OpenAI API.
Context-aware responses based on conversation history.
Simple frontend to interact with the chatbot.
Django backend to handle API requests and serve the chatbot page.
Prerequisites

Before running this project, ensure you have the following installed:
Python 3.x
Django
OpenAI API key
Setup

Step 1: Clone the Repository
Clone this repository to your local machine:
cd chatbot-project

Step 2: Install Dependencies
Install the required Python dependencies using pip:
pip install -r requirements.txt
Alternatively, you can install Django and OpenAI SDK manually:
pip install django openai

Step 3: Configure OpenAI API Key
Set your OpenAI API key in the chatbot/views.py file. For production, it is recommended to store the key in environment variables securely.
OPENAI_API_KEY = "your-api-key-here"

Step 4: Run Migrations
Run Django migrations to set up the database (if needed):
python manage.py migrate

Step 5: Start the Django Development Server
Run the Django development server:
python manage.py runserver
Visit http://127.0.0.1:8000/chatbot/ in your browser to start chatting with the AI.
Create a Virtual Environment

python3 -m venv myenv
Activate the Virtual Environment

source myenv/bin/activate
Install Django and OpenAI SDK
pip install django openai

<img width="1469" alt="Screenshot 2025-03-15 at 10 49 08 PM" src="https://github.com/user-attachments/assets/8a18962c-03ca-4725-b355-ddcb0d1e69b4" />

