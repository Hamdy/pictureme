from django.conf.urls.defaults import *
from pictureme.capture.views import print_picture

urlpatterns = patterns('',
                      url(r'^print$', print_picture),
                      )