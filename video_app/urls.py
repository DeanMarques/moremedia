from django.conf.urls import url
from . import views

app_name = 'video_app'

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^(?P<group_id>[0-9]+)/$', views.detail, name='detail'),
]