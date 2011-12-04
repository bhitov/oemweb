from django.db import models
from datetime import datetime

class Hazard(models.Model):
    submitted_time = models.DateTimeField(auto_now=True)
    submitted_username = models.CharField(max_length = 150)
    source = models.CharField(max_length = 150, blank=True, null=True)
    hazard_type = models.CharField(max_length = 150, blank=True, null=True)
    hazard_subfield_one = models.CharField(max_length = 150, blank=True, null=True)
    hazard_subfield_two = models.CharField(max_length = 150, blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)
    ticket_latitude = models.FloatField(blank=True, null=True)
    ticket_longitude = models.FloatField(blank=True, null=True)
    cleared_time = models.DateTimeField(blank=True, null=True)
    cleared_username = models.CharField(max_length = 150)

class Post(models.Model):
    data = models.CharField(max_length = 150, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
class KML(models.Model):
    #name = models.CharField(max_length = 100)
    file = models.FileField(upload_to="files")
    #filename = models.CharField(max_length=300)
#    filenamex = models.FileField(upload_to="files").name
