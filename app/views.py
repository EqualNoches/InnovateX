from django.shortcuts import render, redirect
from datetime import datetime
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib import messages
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger
from app.models import (
    GeneralInfo,
    Service,
    Testimonial,
    FrequentlyAskedQuestion,
    ContactFormLog,
    Blogs,
)


# Create your views here.
def index(request):

    general_info = GeneralInfo.objects.first()

    services = Service.objects.all()

    testimonials = Testimonial.objects.all()

    faqs = FrequentlyAskedQuestion.objects.all()

    recent_blogs = Blogs.objects.all().order_by("published_date")

    default_value = ""

    context = {
        "company_name": getattr(general_info, "company_name", default_value),
        "location": getattr(general_info, "company_name", default_value),
        "email": getattr(general_info, "email", default_value),
        "phone": getattr(general_info, "phone_number", default_value),
        "open_hours": getattr(general_info, "open_hours", default_value),
        "video_url": getattr(general_info, "video_url", default_value),
        "twitter_url": getattr(general_info, "X_url", default_value),
        "facebook_url": getattr(general_info, "facebook_url", default_value),
        "instagram_url": getattr(general_info, "instagram_url", default_value),
        "linkedin_url": getattr(general_info, "linkedin_url", default_value),
        "services": services,
        "testimonials": testimonials,
        "faqs": faqs,
        "recent_blogs": recent_blogs,
    }

    print(f"context: {context}")
    return render(request, "index.html", context)


def contact_form(request):
    if request.method == "POST":
        print("\n User just submitted contact form\n")
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        context = {
            "name": name,
            "email": email,
            "subject": subject,
            "message": message,
        }
        html_content = render_to_string("email.html", context)

        is_success = False
        error_message = ""
        try:
            send_mail(
                subject=subject,
                message=f"{name} - {email} - {message}",
                html_message=html_content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
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
            name=name,
            email=email,
            subject=subject,
            message=message,
            action_time=timezone.now(),
            is_success=is_success,
            error_message=error_message,
        )

    return redirect("home")


def blog_detail(request, blog_id):
    blog = Blogs.objects.get(id=blog_id)

    recent_blogs = (
        Blogs.objects.all().exclude(id=blog_id).order_by("published_date")[:2]
    )
    context = {"blog": blog, "recent_blogs": recent_blogs}

    return render(request, "assets/blog_details.html", context)


def blogs(request):

    all_blogs = Blogs.objects.all()
    paginator = Paginator(all_blogs, 6)

    print(f"paginated pages: {paginator.num_pages}")

    page = request.GET.get("page")

    blogs = paginator.page(1)

    context = {"all_blogs": blogs}
    return render(request, "assets/blog.html", context)
