from django.conf.urls import url
from . import views

# All urls in this file will be invoked by this format - 'localhost:8000/polls/XXXX', where XXXX is the view that will be invoked.

urlpatterns = [
    url(r'^$', views.index, name='index'), # this is for the url pattern like 'localhost:8000/polls/', where there is nothing after polls
    url(r'page2', views.page2, name='page2'),
    url(r'^detail/(?P<id>\d+)/$', views.detail, name="detail") # ?P - a parameter, <id> - the name of parameter is 'id', \d - it should be a digit
                                                             #, + - should be one or more digit, $ - end of it
];
