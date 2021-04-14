from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Blog(models.Model):
    title = models.CharField(max_length=69)
    body = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.owner}'
