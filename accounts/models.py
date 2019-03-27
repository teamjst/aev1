from django.db import models

# Create your models here.
class Users(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    uname = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.uname
