import openai
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from .models import ChatHistory


# OpenAI API Key 
OPENAI_API_KEY = ""

# Maximum memory (7 exchanges -> 14 messages: 7 user + 7 bot responses)
MAX_MEMORY = 7

@csrf_exempt
def chatbot(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get("user_id")
        user_message = data.get("message")

        if not user_id or not user_message:
            return JsonResponse({"error": "user_id and message are required"}, status=400)
        
        # Fetch or create user chat history
        try:
            chat_entry = ChatHistory.objects.get(user_id=user_id)
            chat_history = chat_entry.conversation
        except ObjectDoesNotExist:
            chat_history = []
            chat_entry = ChatHistory(user_id=user_id, conversation=chat_history)

        # Append user message
        chat_history.append({"role": "user", "content": user_message})

        # Trim history to last 7 exchanges (14 messages)
        chat_history = chat_history[-MAX_MEMORY * 2:]

        # Call OpenAI API
        client = openai.OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=chat_history
        )

        bot_reply = response.choices[0].message.content
        
        # Append bot response to history
        chat_history.append({"role": "assistant", "content": bot_reply})

        # Save updated history
        chat_entry.conversation = chat_history
        chat_entry.save()

        return JsonResponse({
            "reply": bot_reply,
            "history": chat_history
        })
    
    return JsonResponse({"error": "Invalid request"}, status=400)


# View to render chatbot page
def chatbot_page(request):
    return render(request, 'chatbot/chat.html')