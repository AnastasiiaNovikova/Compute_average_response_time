from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^show_response/$', views.show_response, name='show_response'),
]