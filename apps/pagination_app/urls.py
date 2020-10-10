from django.conf.urls import url
from . import views         

urlpatterns = [
    url(r'^$', views.index),

    url(r'^leads/info/$', views.leads_info),



    url(r'^on_load/$', views.on_load),

    # url(r'^leads_by_name/$', views.leads_by_name),

    # url(r'^leads_by_page_num/(?P<page_num>\d+)/$', views.leads_by_page_num),

    # url(r'^leads_by_page_num/$', views.leads_by_page_num),

    # url(r'^leads/info/$', views.leads_info ),

    # url(r'^/$', views. ),

]
