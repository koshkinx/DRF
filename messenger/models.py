from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    name = models.CharField(max_length=100)
    participants = models.ManyToManyField(User, related_name='chats')

    def __str__(self):
        return self.name


class Message(models.Model):
    chat = models.ForeignKey(
        Chat, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(
        User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username}: {self.content[:20]}"
