from django.shortcuts import redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing_brand = request.POST['listing_brand']
        listing_model = request.POST['listing_model']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        #broker_email = request.POST['broker_email']
        broker_email = 'to@aol.com'
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listings/'+listing_id)
        contact = Contact(listing_brand=listing_brand, listing_model=listing_model, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact.save()
        '''
        send_mail("E-Car Listing Inquiry", "There has been an inquiry for " + listing + ". Sign into the admin panel for more info",
        'from@gmail.com', [broker_email, 'cc@yahoo.com',], fail-silently=False)
        '''
        messages.success(request, 'Your request has been submitted, a broker will get back to you soon')
        return redirect('/listings/'+listing_id)
