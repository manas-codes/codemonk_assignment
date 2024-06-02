from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, dob, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, dob=dob)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, dob, password=None):
        user = self.create_user(email, name, dob, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

#Model structure for Registed user
class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'dob']

    def __str__(self):
        return self.email
#Model structure for paragraphs
class Paragraph(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

#Model structure for words
class WordIndex(models.Model):
    word = models.CharField(max_length=255)
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE)
