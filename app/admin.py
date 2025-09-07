from django.contrib import admin
from app.models import (
    GeneralInfo,
    Service,
    Testimonial,
    FrequentlyAskedQuestion,
    ContactFormLog,
    Category,
    Blogs
)

@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):

    list_display = [
        'company_name',
        'location',
        'email',
        'phone_number',
        'open_hours',
    ]

    # # show to disable add permissions
    # def has_add_permission(self, request, obj=None):
    #     return False
    
    # # show to disable update permissions
    # def has_change_permission(self, request, obj = ...):
    #     return False

    # #show to disable delete permissions
    # def has_delete_permission(self, request, obj = ...):
    #     return False

    # #show you can set field to idsable update

    readonly_fields = [
        'email',
    ]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    
    list_display = [
        "title",
        "description",
    ]

    
    search_fields = [
        "title",
        "description",
        ]



@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    
    list_display = [
        "username",
        "user_job_title",
        "display_rating_count",
    ]

    def display_rating_count(self, obj):
        return '*' * obj.rating_count
    
    display_rating_count.short_description = "Rating"

@admin.register(FrequentlyAskedQuestion)
class FrequentlyAskedQuestionsAdmin(admin.ModelAdmin):
    list_display = [
        "question",
        "answer",
    ]


@admin.register(ContactFormLog)
class ContactFormLogAdmin(admin.ModelAdmin):

    list_display = [
        'email',
        'is_success',
        'action_time',
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = [
        'name_of_category',
    ]


@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):

    list_display = [
        'title',
        'author',
        'published_date',
        'category',
        'blog_image'
    ]




