from django import http
from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.views import generic
from .models import *
import bcrypt
from django.contrib import messages # flash messages
from .models import *

from django.core import serializers
from django.core.paginator import Paginator
from datetime import datetime

# ==========================================
def index(request):

    return render(request, 'pagination_app/index.html')
# ---------------------------------------------

def leads_info(request):
    leads = Lead.objects.all()


    # if they entered in the date areas
    if request.POST['date_from']:

        # creating strings in specific format
        # date_from = datetime.datetime.strptime(request.POST['date_from'], '%m/%d/%Y')

        print('-'*30)
        # print(date_from)



    return render(request, "pagination_app/table.html", {"leads": leads})


# ---------------------------------------------
# def leads_info(request):
#     all_leads = Lead.objects.all()
#     pages = Paginator(all_leads, 2)
#     leads_by_page = pages.page(1)

#     return render(request, "ajax_pagination/table.html", {"leads": all_leads})

# ---------------------------------------------
# def on_load(request):

#     # getting page numbers for form
#     page_nums = Lead.objects.values('page_num').distinct().order_by("page_num")

#     return render(request, 'ajax_pagination/page_number.html', {'page_nums': page_nums})

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

