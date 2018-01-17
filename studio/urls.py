from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^task$', views.ShowTask.as_view(), name='show_task'),
    url(r'^task/add/$', views.AddTask.as_view(),name='add_task'),
    url(r'^(?P<slug>[\w\-]+)$', views.ShowTask.as_view(), name='show'),
        ]
