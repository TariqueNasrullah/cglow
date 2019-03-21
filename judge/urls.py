from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.judge_index, name='judge_index'),
    url(r'^(?P<contest_name>[^/]+)/$', views.judger_page, name='judger_page'),
]
