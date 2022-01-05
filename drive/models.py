from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Profile(User):

    def __str__(self):
        return self.username


class Drive(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/', max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    permissions = models.ForeignKey(Profile, on_delete=CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.title
