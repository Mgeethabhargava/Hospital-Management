from django.db import models
from users.models import CustomUser

class Hospital(models.Model):
    name = models.CharField(max_length=255)
    location = models.TextField()

class Appointment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    date = models.DateTimeField()
    token = models.CharField(max_length=10, unique=True)
    diagnosis_status = models.TextField(null=True, blank=True)
    report_url = models.URLField(null=True, blank=True)
