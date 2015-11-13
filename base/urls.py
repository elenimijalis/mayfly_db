from django.conf.urls import patterns, url
from haystack.views import SearchView
from haystack.query import SearchQuerySet
from . import views

# why am I doing this
sqs = SearchQuerySet()

urlpatterns = patterns('haystack.views',
    url(r'^search/', SearchView(template='search/search.html', form_class=views.My_Form), name='haystack_search'),
)
