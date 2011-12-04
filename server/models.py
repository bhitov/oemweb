from django.db import models
from datetime import datetime

class Post(models.Model):
    data = models.CharField(max_length = 150, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
class KML(models.Model):
    name = models.CharField(max_length = 100)
    file = models.FileField(upload_to="files")