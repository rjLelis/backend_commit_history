from django.contrib.auth.models import User
from django.db import models

class Repository(models.Model):

    name = models.CharField(max_length=50, unique=True)

    description = models.CharField(
        max_length=100,
        default='',
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
