# from django.urls import path
# from .views import chatbot, chatbot_page

# urlpatterns = [
#     path('', chatbot_page, name='chatbot_page'),  # Serves chatbot HTML page
#     path('chat/', chatbot, name='chatbot'),  # API endpoint for chatbot responses
# ]
from django.urls import path
from .views import chatbot, chatbot_page

urlpatterns = [
    path('', chatbot_page, name='chatbot_page'),  # Serves chatbot HTML page
    path('chat/', chatbot, name='chatbot'),  # API endpoint for chatbot responses
]