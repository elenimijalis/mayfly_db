from django.db import models

class Journal(models.Model):
    name = models.TextField()

class Paper(models.Model):
    author = models.TextField()
    title = models.TextField()
    date = models.DateField()
    keywords = models.TextField()
    journal = models.ForeignKey(Journal)
