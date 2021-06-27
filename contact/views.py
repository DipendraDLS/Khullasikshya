from django.shortcuts import render, redirect

# For Contact Form to send email
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
import sweetify


# Create your views here.


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact_detail = "Name:" + name + "\nEmail:\t" + email + "\nMessage:\n" + message

        if not request.user.is_authenticated:
            subject = "A Visitor's Comment"
        else:
            subject = str(request.user) + "'s Comment"

        try:
            send_mail(subject,
                      contact_detail,
                      settings.EMAIL_HOST_USER,
                      ['contact@khullasikshya.com'],
                      fail_silently=False)

            msg = True
            return render(request, 'contact/contact.html', {'msg': msg})

        except Exception as e:
            exception = str(e)
            msg = False
            return render(request, 'contact/contact.html', {'msg': msg, 'exception': exception})

    return render(request, 'contact/contact.html')
