from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^show_result/$', views.show_result, name='show_result'),
]