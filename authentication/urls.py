from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^logout/$', views.user_logout, name='user_logout'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.login, name='login'),
]	