from django.db import models

class Keyword(models.Model):
    keyword = models.CharField(max_length=128)

    def __str__(self):
        return self.keyword

class Journal(models.Model):
    name = models.TextField()
    orig_id = models.IntegerField()

    def __str__(self):
        return self.name

class Paper(models.Model):
    author = models.TextField()
    date = models.IntegerField()
    title = models.TextField()
    journal = models.ForeignKey(Journal)
    volume = models.CharField(max_length=64, default='')
    page_start = models.CharField(max_length=64, default='')
    page_end = models.CharField(max_length=64, default='')
    keywords = models.ManyToManyField(Keyword)
    reprint = models.BooleanField(default=False)
    pdf = models.BooleanField(default=False)
    url = models.URLField(default='')

    def __str__(self):
        return self.name + ' | ' + self.author
