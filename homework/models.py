from django.db import models
from django.contrib.postgres.fields import ArrayField
from user.models import User


class Homework(models.Model):
    name = models.CharField(max_length=100, null=False, unique=False)
    description = models.TextField(null=False, unique=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    subjects = ArrayField(
        models.CharField(max_length=150),
        blank=True,
        default=list
    )

    class Meta:
        db_table = 'homework'
