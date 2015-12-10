from django.db import models

class Keyword(models.Model):
    keyword = models.CharField(max_length=128)

    def __str__(self):
        return unicode(self.keyword)

class Journal(models.Model):
    name = models.TextField()
    orig_id = models.IntegerField()

    def __unicode__(self):
        return unicode(self.name)

class Paper(models.Model):
    author = models.TextField()
    date = models.IntegerField(null=True, blank=True)
    title = models.TextField()
    journal = models.ForeignKey(Journal, null=True, blank=True)
    volume = models.CharField(max_length=64, default='')
    page_start = models.CharField(max_length=64, default='')
    page_end = models.CharField(max_length=64, default='')
    keywords = models.ManyToManyField(Keyword)
    reprint = models.BooleanField(default=False)
    lookup = models.CharField(max_length=32, default='')
    pdf = models.FileField(null=True, blank=True)

    def info_string(self):
        info_st = "<i>%s</i> " % self.journal.name
        if self.volume is not "None" and len(self.volume) > 0:
            info_st += "%s, " % self.volume
        if self.page_start is not "None" and len(self.page_start) > 0:
            info_st += "%s " % self.page_start
            if self.page_end is not "None" and len(self.page_end) > 0:
                info_st += "- %s " % self.page_end
        if self.date is not "None" > 0:
            info_st += "(%s)" % self.date
        return info_st

    def keyword_string(self):
        kw_st = (', ').join(['<a href="/?keyword=%s">%s</a>' % (kw.keyword, kw.keyword) for kw in self.keywords.all()])
        return kw_st

    def __unicode__(self):
        return unicode(self.title + ' | ' + self.author)
