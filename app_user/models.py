from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


class MyAppUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, username, password):
        if username is None:
            raise TypeError("Username cannot be empty")
        if email is None:
            raise TypeError("Email cannot be empty")
        if password is None:
            raise TypeError("Password cannot be empty")

        user = self.model(username=username, first_name=first_name, last_name=last_name,
                          email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password, first_name, last_name):
        if username is None:
            raise TypeError("Username cannot be empty")
        if email is None:
            raise TypeError("Email cannot be empty")
        if password is None:
            raise TypeError("Password cannot be empty")

        user = self.create_user(username=username, email=self.normalize_email(email), first_name=first_name,
                                last_name=last_name, password = password)
        user.set_password(password)
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class AppUser(AbstractBaseUser):
    email = models.EmailField(max_length=64, unique=True)
    username = models.CharField(max_length=64, unique=True)
    first_name = models.CharField(max_length=255, unique=False)
    last_name = models.CharField(max_length=255, unique=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyAppUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.username

    def has_perm(self, per, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

