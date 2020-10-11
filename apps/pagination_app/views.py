from django import http
from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.views import generic
from .models import *
import bcrypt
from django.contrib import messages # flash messages
from .models import *

from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from datetime import datetime
from datetimerange import DateTimeRange
import datetime as otherdatetime
import pytz

import re
# ==========================================
def index(request):

    leads_list = Lead.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(leads_list,3)
    leads=paginator.page(1)

    try:
        leads = paginator.page(page)
    except PageNotAnInteger:
        leads = paginator.page(1)
    except EmptyPage:
        leads = paginator.page(paginator.num_pages)

    return render(request, 'pagination_app/index.html', {'leads':leads})
# ---------------------------------------------
# ---------------------------------------------
# get the first page using pagination
def on_load(request):

    leads_list = Lead.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(leads_list,3)
    leads=paginator.page(1)

    return render(request, 'pagination_app/table.html', {'leads': leads })

# ---------------------------------------------

def leads_info(request):

    # getting leads by input of name 
    if request.POST['name']:
        leads = Lead.objects.filter(first_name__startswith=request.POST['name'])

        return render(request, "pagination_app/table.html", {"leads": leads})

    # if they entered in the date areas
    if request.POST['date_from']:
    
        all_leads = Lead.objects.all()

        # creating strings in specific format
        date_from = datetime.strptime(request.POST['date_from'], '%m/%d/%Y')
        date_to = datetime.strptime(request.POST['date_to'], '%m/%d/%Y')

        utc=pytz.UTC
        utc_date_from = date_from.replace(tzinfo=utc)
        utc_date_to = date_to.replace(tzinfo=utc)
 
        # using Python DateTimeRange library
        time_range = DateTimeRange(utc_date_from, utc_date_to)

        a = Lead.objects.first()
        b = a.created_at

        leads = []
        for lead in all_leads:
            
            if lead.created_at in time_range:
                leads.append(lead)
          
        return render(request, "pagination_app/table.html", {"leads": leads})
    
# ---------------------------------------------

def leads_list(request, pNum):

    print('-"*30')
    print(pNum)

    leads_list = Lead.objects.all()
    page = request.GET.get('page')

    paginator = Paginator(leads_list,3)
    leads=paginator.page(pNum)

    return render(request, 'pagination_app/table.html', {'leads': leads })

