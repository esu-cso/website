from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models.fields import UUIDField
import uuid


# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)

class UserProfile(models.Model):
  # id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
   # user = models.OneToOneField(User, on_delete=models.CASCADE)
    test = models.CharField(max_length=25)