import openai
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# OpenAI API Key 
OPENAI_API_KEY = ""

# Store conversation history (in-memory for now, can use DB later)
chat_history = []

@csrf_exempt
def chatbot(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get("message", "")
        
        # Append user message to history
        chat_history.append({"role": "user", "content": user_message})
        
        # Create OpenAI client
        client = openai.OpenAI(api_key=OPENAI_API_KEY)
        
        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=chat_history
        )
        
        bot_reply = response.choices[0].message.content
        
        # Append bot response to history
        chat_history.append({"role": "assistant", "content": bot_reply})
        
        return JsonResponse({"reply": bot_reply})
    return JsonResponse({"error": "Invalid request"})

# View to render chatbot page
def chatbot_page(request):
    return render(request, 'chatbot/chat.html')