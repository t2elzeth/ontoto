from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class Chat(models.Model):
    first_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats')
    second_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats')

    def __str__(self):
        return "{} and {}".format(self.first_user.get_username(), self.second_user.get_username())


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    text = models.TextField()

    date_sent = models.TimeField(default=timezone.now)

    def __str__(self):
        return "{} in {}".format(self.text[:10], self.chat)
