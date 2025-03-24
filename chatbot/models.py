from django.db import models

class ChatHistory(models.Model):
    user_id = models.CharField(max_length=255, unique=True)
    conversation = models.JSONField(default=list)  # Stores chat history as JSON

    def __str__(self):
        return f"ChatHistory(User: {self.user_id})"
