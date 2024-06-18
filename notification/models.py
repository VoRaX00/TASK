# from django.db import models
# from user_app.models import User
# from car_cargo.models import Cargo, Car
#
# MAYBECHOICE = (
#     ('y', 'Yes'),
#     ('n', 'No'),
#     ('u', 'Unknown'),
# )
#
#
# class NotifyCargo(models.Model):
#     first_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='first_user_cargo_notify')
#     second_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='second_user_cargo_notify')
#
#     cargo = models.ForeignKey(Cargo, null=False, on_delete=models.CASCADE)
#
#     status_first_user = models.CharField(max_length=1, choices=MAYBECHOICE, default='y')
#     status_second_user = models.CharField(max_length=1, choices=MAYBECHOICE, default='u')
#
#     comment_first_user = models.TextField(null=True, unique=False)
#     comment_second_user = models.TextField(null=True, unique=False)
#
#     class Meta:
#         db_table = 'notify_cargo'
#
#
# class NotifyCar(models.Model):
#     first_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='first_user_notify')
#     second_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='second_user_notify')
#
#     car = models.ForeignKey(Car, null=False, on_delete=models.CASCADE)
#
#     status_first_user = models.CharField(max_length=1, choices=MAYBECHOICE, default='y')
#     status_second_user = models.CharField(max_length=1, choices=MAYBECHOICE, default='u')
#
#     comment_first_user = models.TextField(null=True, unique=False)
#     comment_second_user = models.TextField(null=True, unique=False)
#
#     class Meta:
#         db_table = 'notify_car'
