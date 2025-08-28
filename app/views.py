from django.shortcuts import render
from datetime import datetime
from app.models import GeneralInfo, Service
# Create your views here.
def index(request):

    general_info = GeneralInfo.objects.first()

    services = Service.objects.all()

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

        "services":  services
    }

    print(f"context: {context}")
    return render(request, "index.html", context)



