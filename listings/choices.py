from listings.models import Listing

listings = Listing.objects.all().filter(is_published=True)

brand_model_choices = {'Reset Both Brand and Model (Any)': ''} | {listing.brand + '  ' + listing.model: listing.brand + '~' + listing.model for listing in listings}

colors_set = {listing.color for listing in listings}
color_choices = {'Reset Color (Any)': ''} | {color: color for color in colors_set}

max_price = max({listing.price for listing in listings})
grade = 200000
budget_choices = {'Reset Budget (Any)': '0'} | {'HK$'+f'{g:,}': str(g) for g in range(grade, max_price + grade, grade)}

hand_drives_set = {listing.hand_drive for listing in listings}
hand_drive_choices = {'Reset Hand Drive (Any)': ''} | {hand_drive + '-hand-drive': hand_drive for hand_drive in hand_drives_set}

wheels_drives_set = {listing.wheels_drive for listing in listings}
wheels_drive_choices = {'Reset Wheels Drive (Any)': ''} | {wheels_drive + '-wheels-drive': wheels_drive for wheels_drive in wheels_drives_set}
