from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.get_title, name='get_title'),
    url(r'^search/(?P<pk>[0-9]+)/$', views.paper_detail, name='paper_detail'),
]
