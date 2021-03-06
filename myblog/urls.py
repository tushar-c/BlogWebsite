from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^blog', views.post_list, name='post_list'),
    url(r'^about', views.about, name='about'),
    url(r'^post/(?P<pk>\d+)/$', views.post_view, name='post_view'),
]
