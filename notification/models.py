from django.db import models
from user.models import User
from homework.models import Homework

MAYBECHOICE = (
    ('y', 'Yes'),
    ('n', 'No'),
    ('u', 'Unknown'),
)


class NotifyHomework(models.Model):
    first_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='first_user_notify')
    second_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='second_user_notify')

    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)

    status_first_user = models.CharField(max_length=1, choices=MAYBECHOICE, default='y')
    status_second_user = models.CharField(max_length=1, choices=MAYBECHOICE, default='u')

    class Meta:
        db_table = 'notify_homework'
