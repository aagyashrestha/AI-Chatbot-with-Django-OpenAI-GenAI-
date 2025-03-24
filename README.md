AI Chatbot with Django & OpenAI (GenAI)

This project is a Generative AI (GenAI) chatbot built using Django and the OpenAI API. It allows users to interact with an AI-powered chatbot that responds to user input with context-based replies. The chatbot stores conversation history and maintains context throughout the session, leveraging OpenAI's GPT-3.5 model for generating dynamic, human-like responses.

#Features

-Generative AI (GenAI) powered chatbot using OpenAI's GPT-3.5 model.

-Basic chat functionality using the OpenAI API.

-Context-aware responses based on conversation history, allowing the chatbot to remember prior exchanges.

-Simple frontend to interact with the chatbot, including a text input and display area for the conversation.

-Django backend to handle API requests, manage user session data, and serve the chatbot page.

-Memory Management: The chatbot stores up to 7 exchanges (14 messages: 7 user + 7 bot) to maintain conversation context.

-Conversation Limit: Once the user and bot have exchanged 7 messages (7 user + 7 bot), the chatbot will automatically trim the conversation history to the most recent exchanges to prevent excessive memory usage. This ensures the chatbot retains context within the memory limit and continues providing relevant, context-aware responses.

<img width="849" alt="Screenshot 2025-03-24 at 11 20 46 AM" src="https://github.com/user-attachments/assets/8e31743b-3cbe-4751-85d6-0cffd46c851d" />

<img width="1336" alt="Screenshot 2025-03-24 at 8 14 54 PM" src="https://github.com/user-attachments/assets/a5954ef9-d8c6-40f0-a609-d8e19134f1d6" />



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


