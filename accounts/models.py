from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField
from portal.models import Category


class User(AbstractUser):
    phone_number = models.CharField(max_length=20)
    category = models.ForeignKey(Category, related_name='users', on_delete=models.CASCADE, null=True, blank=True) 

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#     category = models.CharField(max_length=100)

#     def __str__(self):
#         return f'Profile for {self.user}'

