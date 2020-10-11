from django.conf.urls import url
from . import views         

urlpatterns = [
    url(r'^$', views.index),

    url(r'^leads/info/$', views.leads_info),

    url(r'^on_load/$', views.on_load),

    url(r'^leads_list/(?P<pNum>\w+)/$', views.leads_list ),

]
