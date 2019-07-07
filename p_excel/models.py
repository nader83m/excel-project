from django.db import models
from django.utils import timezone
from datetime import datetime

class IPC_Codes(models.Model):
    code = models.CharField(max_length = 10)
    title = models.TextField()
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return '<Code: {}, Title: {}, Date {}>'.format(self.code, self.title, self.date)

class Inventions(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField()
    title = models.TextField()
    untype = models.CharField(max_length=50)
    patent = models.CharField(max_length=50)
    classification = models.CharField(max_length=50)
    inventor = models.TextField()
    year_week = models.CharField(max_length=50)
    date = models.DateTimeField(default = timezone.now)

class Excel_Files(models.Model):
    code = models.CharField(max_length=10)
    title=models.TextField()
    filename=models.CharField(max_length=50)
    year_week = models.CharField(max_length=50)

