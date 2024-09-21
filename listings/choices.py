from listings.models import Listing

listings = Listing.objects.all().filter(is_published=True)

brand_model_choices = {('Reset Brand (Any)'.center(20) + ' ' + 'Reset Model (Any)'.center(25)): ''}.update({(listing.brand.center(20)[:20] + ' ' + listing.model.center(25)[:25]): (listing.brand.ljust(20)[:20] + listing.model.ljust(25)[:25]) for listing in listings})
    
colors_set = {listing.color for listing in listings}
color_choices = {'Reset Color (Any)': ''}.update({color: color for color in colors_set})

price_choices = {
    'Reset Max Price (Any)': '0',
    '$200,000': '200000',
    '$400,000': '400000',
    '$600,000': '600000',
    '$800,000': '800000',
    '$1,000,000': '1000000',
    '$1,200,000': '1200000',
    '$1,400,000': '1400000',
    '$1,600,000': '1600000',
    '$1,800,000': '1800000',
    '$2M+': '2000000',
}

hand_drive_choices = {
    'Reset Hand Drive (Any)': '', 
    'Right-hand-drive': 'right',
    'Left-hand-drive': 'left',
}

wheels_drive_choices = {
    'Reset Wheels Drive (Any)': '',
    'Four-wheels-drive': '4',
    'Two-wheels-drive': '2',
}
