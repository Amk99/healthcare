from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError


# Create your models here.
class testimonies(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    img = models.ImageField(upload_to = 'pics')
    date = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name
    
    
class contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = PhoneNumberField()
    message = models.TextField() 
    
    
    def __str__(self):
        return self.name
    

class my_blog(models.Model):
    title = models.CharField(max_length = 200)
    quote = models.CharField(max_length = 500,null=True,blank = True)
    intro = models.TextField(null=True,blank=True)
    content = models.TextField(null=True)
    image_one = models.ImageField(upload_to='pics')
    image_two = models.ImageField(upload_to='pics',null = True)    
    
    def __str__(self):
        return self.title   


def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and obj.id != model.objects.get().id):
        raise ValidationError("Can only create one instance")
    

      
class SiteEditor(models.Model):
    home_Page_title_one = models.CharField(max_length=250)
    home_Page_title_two = models.CharField(max_length=250)
    home_page_title_background = models.ImageField(upload_to = 'pics',default = "pics/hero_1.jpg")
    home_page_title_background_two = models.ImageField(upload_to = 'pics',default="pics/hero_2.jpg")
    home_page_image_one = models.ImageField(upload_to = 'pics',default='pics\img_4.jpg')
    home_page_text_one = models.TextField()
    home_page_image_two = models.ImageField(upload_to = 'pics',default='pics\img_3.jpg')
    home_page_text_two = models.TextField()
    about_image = models.ImageField(upload_to = 'pics',default = 'pics\image_6.jpg')
    about_text = models.TextField(null = True)
    
    def clean(self):
        validate_only_one_instance(self)

    def __str__(self):
        return "site editor"