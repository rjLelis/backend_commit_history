from django.db import models
from django.utils import timezone

class Repository(models.Model):

    name = models.CharField(max_length=50, unique=True)

    description = models.CharField(
        max_length=100,
        default='',
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(default=timezone.now)
