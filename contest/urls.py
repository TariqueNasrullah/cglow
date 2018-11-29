from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.contest_list, name='contest'),
	url(r'^(?P<pk>\d+)$', views.contest_info, name='contest_info'),
	url(r'^(?P<pk>\d+)/dashboard$', views.contest_dashboard, name='contest_dashboard'),
	url(r'^(?P<pk>\d+)/dashboard/(?P<problem_id>\d+)$', views.contest_show_problem, name='contest_show_problem'),
	url(r'^(?P<pk>\d+)/submission$', views.contest_individual_submission, name='contest_individual_submission'),
	url(r'^(?P<pk>\d+)/standing$', views.contest_standing, name='contest_standing'),
	url(r'^contest_standing_server/(?P<pk>\d+)/$', views.contest_standing_server, name='contest_standing_server'),
]