from django.shortcuts import render, redirect
from datetime import datetime
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib import messages
from django.utils import timezone
from app.models import (
    GeneralInfo, 
    Service,
    Testimonial,
    FrequentlyAskedQuestion,
    ContactFormLog
)
# Create your views here.
def index(request):

    general_info = GeneralInfo.objects.first()
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    faqs = FrequentlyAskedQuestion.objects.all()
    context = {
        "company_name": general_info.company_name,
        "location": general_info.location,
        "email" : general_info.email,
        "phone": general_info.phone_number,
        "open_hours" : general_info.open_hours,
        "video_url" : general_info.video_url,
        "twitter_url" : general_info.X_url,
        "facebook_url" : general_info.facebook_url,
        "instagram_url" : general_info.instagram_url,
        "linkedin_url" : general_info.linkedin_url,
        "services":  services,
        "testimonials" : testimonials,
        'frequently_asked_question': faqs,
    }

    print(f"context: {context}")
    return render(request,"index.html",context)

def contact_form(request):
    if request.method == "POST":
        print("\n User just submitted contact form\n")
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        context = {
            "name" : name,
            "email": email,
            "subject": subject,
            "message": message,
        }
        html_content = render_to_string('email.html', context)
        
        is_success = False
        error_message = ""
        try:
            send_mail(
                subject = subject,
                message = f"{name} - {email} - {message}",
                html_message=html_content,
                from_email = settings.EMAIL_HOST_USER,
                recipient_list = [settings.EMAIL_HOST_USER],
                fail_silently = False
            )
            
        except Exception as e:
            is_success = False
            error_message = str(e)
            messages.error(request, "There is an error, the email couldn't get sent")

        else:
            is_success = True
            error_message = f"Email was sent from {name}"
            messages.success(request, "The email was sent")

        ContactFormLog.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message,
            action_time = timezone.now(),
            is_success = is_success,
            error_message = error_message,
        )

    return redirect('home')

