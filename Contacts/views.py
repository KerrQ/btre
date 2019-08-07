from django.shortcuts import redirect
from django.core.mail import send_mail
from .models import Inquiry
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def inquiry_page(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        listing = request.POST['listing']
        message = request.POST['message']
        listing_id = request.POST['listing_id']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        print(listing_id)
        if request.user.is_authenticated:
            user_id = request.user.id
            has_inquiry = Inquiry.objects.all().filter(listing_id=listing_id, user_id=user_id)
            print(has_inquiry)
            if has_inquiry:
                messages.error(request, 'you have already made an inquiry')
                return redirect('/listings/' + listing_id)

        inquiry = Inquiry(name=name,
                          email=email,
                          phone=phone,
                          message=message,
                          listing=listing,
                          listing_id=listing_id,
                          user_id=user_id)
        inquiry.save()
        messages.success(request, 'you made inquiry successfully')
        send_mail(listing, message, email, [realtor_email, 'muhammadreda4444@gmail.com'], fail_silently=False)
        return redirect('/listings/'+listing_id)
    return redirect('/listings/')
