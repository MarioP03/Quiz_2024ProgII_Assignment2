from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class PublicQuestions(models.Model):
    title = models.CharField(max_length=1000, unique=True)
    a = models.CharField(max_length=100, unique=False)
    b = models.CharField(max_length=100, unique=False)
    c = models.CharField(max_length=100, unique=False)
    d = models.CharField(max_length=100, unique=False)
    correct_answer = models.CharField(max_length=1, unique=False)
    diff = models.CharField(max_length=20, unique=False)
    topic = models.CharField(max_length=100, unique=False)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'PublicQuestions'


class UsersManager(BaseUserManager):
    def create_user(self, username, password=None, points = 0):
        if not username:
            raise ValueError('The username field must be set')
        email = self.normalize_email(email)
        user = self.model(email = email, username = username, points = points)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser has to have is_staff being True')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser has to have is_superuser being True')
        
        user = self.create_user(username = username, password = password, **extra_fields)
        user.is_admin = True
        user.save(using=self._db)
        return user

class Users(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    points = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UsersManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_admin
    
    class Meta:
        db_table = 'Users'

class Leaderboard(models.Model):
    username = models.CharField(max_length=100)
    points = models.IntegerField()
    date_achieved = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.username} - {self.points}'
    
    class Meta:
        db_table = 'Leaderboard'