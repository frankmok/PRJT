from django.shortcuts import render
from listings.models import Listing
from brokers.models import Broker
from listings.choices import budget_choices, brand_model_choices, color_choices, hand_drive_choices, wheels_drive_choices
from bcec.company import company_website, company_phone, company_email

# Create your views here.

def index(request):
    default_newly_listing_no = 3
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:default_newly_listing_no]
    context = {
    'listings': listings,
    'default_newly_listing_no': default_newly_listing_no,
    'budget_choices': budget_choices,
    'brand_model_choices': brand_model_choices,
    'color_choices': color_choices,
    'hand_drive_choices': hand_drive_choices,
    'wheels_drive_choices': wheels_drive_choices,
    'company_website': company_website,
    'company_phone': company_phone,
    'company_email': company_email,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    context = {
    'company_website': company_website,
    'company_phone': company_phone,
    'company_email': company_email,
    }
    return render(request, 'pages/about.html', context)

def history(request):
    context = {
    'company_website': company_website,
    'company_phone': company_phone,
    'company_email': company_email,
    }
    return render(request, 'pages/history.html', context)

def vision(request):
    context = {
    'company_website': company_website,
    'company_phone': company_phone,
    'company_email': company_email,
    }
    return render(request, 'pages/vision.html', context)

def goals(request):
    context = {
    'company_website': company_website,
    'company_phone': company_phone,
    'company_email': company_email,
    }
    return render(request, 'pages/goals.html', context)

def organization(request):
    context = {
    'company_website': company_website,
    'company_phone': company_phone,
    'company_email': company_email,
    }
    return render(request, 'pages/organization.html', context)

def work(request):
    context = {
    'company_website': company_website,
    'company_phone': company_phone,
    'company_email': company_email,
    }
    return render(request, 'pages/work.html', context)

def team(request):
    brokers = Broker.objects.order_by('-hire_date')
    context = {
    'brokers': brokers,
    'company_website': company_website,
    'company_phone': company_phone,
    'company_email': company_email,
    }
    return render(request, 'pages/team.html', context)

def mvb(request):
    mvp_brokers = Broker.objects.all().filter(is_mvp=True)
    context = {
    'mvp_brokers': mvp_brokers,
    'company_website': company_website,
    'company_phone': company_phone,
    'company_email': company_email,
    }
    return render(request, 'pages/mvb.html', context)

def pdpolicy(request):
    context = {
    'company_website': company_website,
    'company_phone': company_phone,
    'company_email': company_email,
    }
    return render(request, 'pages/pdpolicy.html', context)

def pcpolicy(request):
    context = {
    'company_website': company_website,
    'company_phone': company_phone,
    'company_email': company_email,
    }
    return render(request, 'pages/pcpolicy.html', context)

def ftpolicy(request):
    context = {
    'company_website': company_website,
    'company_phone': company_phone,
    'company_email': company_email,
    }
    return render(request, 'pages/ftpolicy.html', context)

def esgpolicy(request):
    context = {
    'company_website': company_website,
    'company_phone': company_phone,
    'company_email': company_email,
    }
    return render(request, 'pages/esgpolicy.html', context)

def ohspolicy(request):
    context = {
    'company_website': company_website,
    'company_phone': company_phone,
    'company_email': company_email,
    }
    return render(request, 'pages/ohspolicy.html', context)

def amlpolicy(request):
    context = {
    'company_website': company_website,
    'company_phone': company_phone,
    'company_email': company_email,
    }
    return render(request, 'pages/amlpolicy.html', context)

def abcpolicy(request):
    context = {
    'company_website': company_website,
    'company_phone': company_phone,
    'company_email': company_email,
    }
    return render(request, 'pages/abcpolicy.html', context)

def joinus(request):
    context = {
    'company_website': company_website,
    'company_phone': company_phone,
    'company_email': company_email,
    }
    return render(request, 'pages/joinus.html', context)

def contactus(request):
    context = {
    'company_website': company_website,
    'company_phone': company_phone,
    'company_email': company_email,
    }
    return render(request, 'pages/contactus.html', context)

def sitemap(request):
    context = {
    'company_website': company_website,
    'company_phone': company_phone,
    'company_email': company_email,
    }
    return render(request, 'pages/sitemap.html', context)

def disclaimer(request):
    context = {
    'company_website': company_website,
    'company_phone': company_phone,
    'company_email': company_email,
    }
    return render(request, 'pages/disclaimer.html', context)

def awarrange(request):
    context = {
    'company_website': company_website,
    'company_phone': company_phone,
    'company_email': company_email,
    }
    return render(request, 'pages/awarrange.html', context)
