from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Task(models.Model):
    task = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(null=True)
    add_date = models.DateTimeField(default=timezone.now)
    is_finished = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
