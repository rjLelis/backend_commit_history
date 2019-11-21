from django.db import models


class Owner(models.Model):

    name = models.CharField(max_length=50, unique=True)

    email = models.EmailField()

class Repository(models.Model):

    name = models.CharField(max_length=50, unique=True)

    description = models.CharField(
        max_length=100,
        default='',
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(Owner, related_name='repositories', on_delete=models.CASCADE)

