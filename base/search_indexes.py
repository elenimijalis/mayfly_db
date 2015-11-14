import datetime
from haystack import indexes
from base.models import Paper, Journal, Keyword

class PaperIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    date = indexes.IntegerField(model_attr='date', null=True)

    def get_model(self):
        return Paper

    def index_queryset(self, using=None):
        """ Used when the entire index for model is updated """
        return self.get_model().objects.all()
