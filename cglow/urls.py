from . import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('home.urls')),
    url(r'^contest/', include('contest.urls')),
    url(r'^authentication/', include('authentication.urls')),
    url(r'^problemset/', include('offlineProblemSolve.urls')),
    url(r'^judge/', include('judge.urls')),
    #websocket purpose
    url(r'^adminstrator/', include('chat.urls')),
    url(r'^clearification/', include('clearification.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)