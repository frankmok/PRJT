from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import budget_choices, brand_model_choices, color_choices, hand_drive_choices, wheels_drive_choices
from bcec.company import company_website, company_phone, company_email

# Create your views here.
def index(request):
    # get all data from listing database
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    pagination = 3
    paginator = Paginator(listings, pagination)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    # pass database records into listings context
    context = {
    'listings': paged_listings,
    'total': len(listings),
    'company_website': company_website,
    'company_phone': company_phone,
    'company_email': company_email,
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
    'listing': listing,
    'company_website': company_website,
    'company_phone': company_phone,
    'company_email': company_email,
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date').filter(is_published=True)
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    if 'brand_model' in request.GET:
        brand_model = request.GET['brand_model']
        if brand_model:
            i = brand_model.index('~')
            queryset_list = queryset_list.filter(brand__iexact=brand_model[:i]).filter(model__iexact=brand_model[i+1:])
    if 'color' in request.GET:
        color = request.GET['color']
        if color:
            queryset_list = queryset_list.filter(color__iexact=color)
    if 'budget' in request.GET:
        budget = int(request.GET['budget'])
        if budget:
            queryset_list = queryset_list.filter(price__lte=budget)
    if 'hand_drive' in request.GET:
        hand_drive = request.GET['hand_drive']
        if hand_drive:
            queryset_list = queryset_list.filter(hand_drive__iexact=hand_drive)
    if 'wheels_drive' in request.GET:
        wheels_drive = request.GET['wheels_drive']
        if wheels_drive:
            queryset_list = queryset_list.filter(wheels_drive__iexact=wheels_drive)
    context = {
    'listings': queryset_list,
    'budget_choices': budget_choices,
    'brand_model_choices': brand_model_choices,
    'color_choices': color_choices,
    'hand_drive_choices': hand_drive_choices,
    'wheels_drive_choices': wheels_drive_choices,
    'values': request.GET,
    'total': len(queryset_list),
    'company_website': company_website,
    'company_phone': company_phone,
    'company_email': company_email,
    }
    return render(request, 'listings/search.html', context)
