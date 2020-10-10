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

        # print('-'*30)
        # print(utc_date_from)
        # print(utc_date_to)
        # print('first_entry_leads created_at')
        # print(b)
        # print(b in time_range)
        leads = []
        for lead in all_leads:
            
            if lead.created_at in time_range:
                leads.append(lead)
                print('*'*30)
                print(leads)
        # for value in time_range.range(otherdatetime.timedelta(days=1)):
        #     for lead in leads:
        #         if lead.created_at in time_range.range:
        #             print('-'*30)
        #             print("match")

        # if date_from < a_time < date_to:
        #     print('date between')
        
        # else: 
        #     print('not between')
      
        return render(request, "pagination_app/table.html", {"leads": leads})
    



# ---------------------------------------------

# def leads_by_name(request):

#     leads = Lead.objects.filter(first_name__startswith=request.POST['name_starts_with'])

#     print("-"*30)
#     print(leads)

#     return render(request, "pagination/table.html", {"leads":leads})



# ---------------------------------------------
# def leads_by_page_num(request, page_num):
# def leads_by_page_num(request):


#     leads = Lead.objects.filter(page_num = request.POST['page_num'])
#     print("="*30)
#     print(request.POST['page_num'])
#     print(leads)


    
#     return render(request, 'ajax_pagination/table.html', {'leads': leads})


# ---------------------------------------------
# def leads_by_page_num(request):

#     all_leads = Lead.objects.all()
#     pages = Paginator(all_leads, 2)
#     leads_by_page = pages.page(1)

#     return render(request, "ajax_pagination/table_copy.html", {"leads": all_leads})

