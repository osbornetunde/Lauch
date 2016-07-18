from django.conf.urls import url

from . import views

urlpatterns = [
      # Homepage
      url(r'^$', views.home, name='home'),
     # url(r'^testhome$', views.testhome, name='testhome'),
      url(r'^(?P<ref_id>.*)$', views.share, name='share'),
      ]
