from django.shortcuts import render
from listings.models import Listing
from brokers.models import Broker
from listings.choices import price_choices, brand_model_choices, color_choices, hand_drive_choices, wheels_drive_choices

# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {'listings': listings,
    'price_choices': price_choices,
    'brand_model_choices': brand_model_choices,
    'color_choices': color_choices,
    'hand_drive_choices': hand_drive_choices,
    'wheels_drive_choices': wheels_drive_choices,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    brokers = Broker.objects.order_by('-hire_date')
    mvp_brokers = Broker.objects.all().filter(is_mvp=True)
    context = {'brokers': brokers, 'mvp_brokers': mvp_brokers}
    return render(request, 'pages/about.html', context)
