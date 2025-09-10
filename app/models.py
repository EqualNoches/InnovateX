from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class GeneralInfo(models.Model):
    company_name = models.CharField(max_length=255, default="Company")
    location= models.CharField(max_length=255 )
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    open_hours = models.CharField(max_length=100, blank= True, null=True)
    video_url= models.URLField(blank=True, null=True)
    X_url= models.URLField(blank=True, null=True)
    facebook_url= models.URLField(blank=True, null=True)
    instagram_url= models.URLField(blank=True, null=True)
    linkedin_url= models.URLField(blank=True, null=True)

    def __str__(self):
        return self.company_name

class Service(models.Model):
    icon = models.CharField(max_length=50, blank= True, null = True)
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    user_image = models.CharField(max_length=225, blank = True, null = True)
    stars_count = [
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five'),
    ]
    rating_count = models.IntegerField( choices= stars_count)
    username = models.CharField(max_length=50)
    user_job_title = models.CharField(max_length=50)
    review = models.TextField()

    def __str__(self):
        return f"{self.username} - {self.user_job_title}"

class FrequentlyAskedQuestion(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question

class ContactFormLog(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField( max_length=254)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    action_time = models.DateTimeField(null = True, blank=True)
    is_success = models.BooleanField(default=False)
    error_message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.email

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null= True, blank=True)
    Country= models.CharField(max_length=50)
    joined_at = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.first_name


class Category(models.Model):
    name_of_category = models.CharField(max_length=50)

    def __str__(self):
        return self.name_of_category

class Blogs(models.Model):
    blog_image = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True, blank=False)
    published_date = models.DateField(blank= False, default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    content = RichTextField()

    def __str__(self):
        return self.title()