from django.db import models
from django.utils import timezone


# Create your models here.
class File(models.Model):
    file_name = models.CharField(max_length=200)
    version = models.CharField(max_length=200)
    file = models.FileField(blank=False, null=False)
    pub_date = models.DateTimeField(auto_now_add=True)
