from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
import uuid
from django.dispatch import receiver 
from django.db.models.signals import post_save



# Create your models here.

class UserProfile(models.Model):
    roles = [
       ('M', 'Member'),
       ('BM', 'Board Member'),
       ('F', 'Faculty')
    ]
    privacy = [
       ('PU', 'Public'),
       ('MO', 'Members Only'),
       ('PR', 'Private')
    ]
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.OneToOneField(User, related_name="userprofile", on_delete=models.CASCADE, null=True, blank=False)
    profileimage = models.ImageField(upload_to ='static/images/userupload/userprofileimage', null=True, blank=True)
    role = models.CharField(max_length=15, blank=True, null=True, choices=roles, default='M')
    privacysettings = models.CharField(max_length=15, blank=False, null=False, choices=privacy, default='MO')
    personalpage = models.BooleanField(blank=False, default=False)
    bio = models.TextField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)


    def __str__(self):
      return str(self.user)
    

    @receiver(post_save, sender=User)
    def CreateProfile(sender, instance, created, **kwargs):
      if created:
        UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def SaveProfile(sender, instance, **kwargs):
      instance.userprofile.save()


    