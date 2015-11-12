from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.paper_list, name='paper_list'),
    url(r'^search/', include('haystack.urls')),
]
