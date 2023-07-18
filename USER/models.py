from django.db import models
import uuid
from django.db import models
import random

class Credentials(models.Model):
    userId = models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    username = models.CharField(max_length=50, blank=True, null=True)
    pseudo = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.username)