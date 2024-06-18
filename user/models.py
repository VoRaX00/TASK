from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone


class CustomUserManager(UserManager):
    use_in_migrations = True

    def _create_user(self, name, phone, email, password, **extra_fields):
        if not email:
            raise ValueError("Вы не указали эл. почту")
        elif not name:
            raise ValueError("Вы не указали имя")
        elif not password:
            raise ValueError("Вы не указали пароль")

        email = self.normalize_email(email)
        user = self.model(name=name, email=email, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_user(self, name=None, email=None, phone=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(name=name, phone=phone, email=email, password=password, **extra_fields)

    def create_superuser(self, name=None, email=None, phone=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(name, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255, blank=True, default='')
    email = models.EmailField(blank=True, default='', unique=True)
    phone = models.BigIntegerField(null=True, unique=False)
    about_me = models.TextField(max_length=700, null=False, default='Пусто', unique=False)
    image = models.ImageField(upload_to='user_images', default='user_images/default.svg', unique=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Mete:
        verbose_name = 'User'
        verbose_name_pluar = 'Users'

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name or self.email.split('@')[0]
