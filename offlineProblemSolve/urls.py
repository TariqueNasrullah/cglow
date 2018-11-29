from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.problem_list, name='problem_list'),
	url(r'^(?P<pk>\d+)/$', views.show_problem, name='show_problem'),
	url(r'^submission/$', views.show_submission, name='show_submission'),
	url(r'^submission/(?P<pk>\d+)/$', views.individual_submission, name='individual_submission'),
]