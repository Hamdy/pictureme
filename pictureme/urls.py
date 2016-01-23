from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from pictureme.capture.views import index

urlpatterns = patterns('',
     url('^$', index),
     url('', include('pictureme.capture.urls')),
)

urlpatterns += staticfiles_urlpatterns()

