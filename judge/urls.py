from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.judge_index, name='judge_index'),
    url(r'^(?P<contest_name>[^/]+)/$', views.judger_page, name='judger_page'),
    url(r'^contestant_submitted_code/(?P<pk>\d+)/$', views.contestant_submitted_code, name='contestant_submitted_code'),
]
