from listings.models import Listing

listings = Listing.objects.all().filter(is_published=True)

brands_set = {listing.brand for listing in listings}
brand_choices = {brand: brand for brand in brands_set}

models_set = {listing.model for listing in listings}
model_choices = {model: model for model in models_set}

origins_set = {listing.origin for listing in listings}
origin_choices = {origin: origin for origin in origins_set}

price_choices = {
    '200000': '$200,000',
    '400000': '$400,000',
    '600000': '$600,000',
    '800000': '$800,000',
    '1000000': '$1,000,000',
    '1200000': '$1,200,000',
    '1400000': '$1,400,000',
    '1600000': '$1,600,000',
    '1800000': '$1,800,000',
    '2000000': '$2M+',
}
