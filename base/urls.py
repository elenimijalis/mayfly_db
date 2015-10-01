from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.paper_list, name='paper_list'),
]
