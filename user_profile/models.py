from django.db import models
from account.models import MyUser

class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images', blank=True, null = True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.email