from listings.models import Listing

listings = Listing.objects.all().filter(is_published=True)

brand_model_choices = {'Reset Both Brand and Model (Any)': ''} | {listing.brand + '  ' + listing.model: listing.brand + '~' + listing.model for listing in listings}

colors_set = {listing.color for listing in listings}
color_choices = {'Reset Color (Any)': ''} | {color: color for color in colors_set}

budget_choices = {
    'Reset Budget (Any)': '0',
    'HK$200,000': '200000',
    'HK$400,000': '400000',
    'HK$600,000': '600000',
    'HK$800,000': '800000',
    'HK$1,000,000': '1000000',
    'HK$1,200,000': '1200000',
    'HK$1,400,000': '1400000',
    'HK$1,600,000': '1600000',
    'HK$1,800,000': '1800000',
    'HK$2M+': '2000000',
}

hand_drive_choices = {
    'Reset Hand Drive (Any)': '', 
    'Right-hand-drive': 'Right',
    'Left-hand-drive': 'Left',
}

wheels_drive_choices = {
    'Reset Wheels Drive (Any)': '',
    'Four-wheels-drive': 'Four',
    'Two-wheels-drive': 'Two',
}
