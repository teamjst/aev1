from django.db import models

# Create your models here.


class Settings(models.Model):
    uName = models.CharField(max_length=25)
    brightness = models.IntegerField(default=100)
    ColorTemp = models.IntegerField(default=2700)
    hue = models.IntegerField(default=359)
    address = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    power: models.BooleanField(default=True)
    sat = models.IntegerField(default=100)
    ip = models.CharField(max_length=25)

    def __str__(self):
        return self.ip