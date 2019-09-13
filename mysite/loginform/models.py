from django.db import models

# Create your models here.
"""class MyObject(models.Model):

    image_url = models.CharField()

    def image_url(self):
        if os.path.exists(self.image_url)
            return self.image_url
        return 'default_image'"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
