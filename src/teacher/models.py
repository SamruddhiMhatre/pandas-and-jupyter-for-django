from django.db import models

# Create your models here.


class Teachers(models.Model):
    name = models.CharField(max_length=250)
    subjects = models.TextField(max_length=250)