from django.db import models

from accounts.models import Profile


class Task(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    archived = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)
