from django.db import models

# Create your models here.

class HomePage(models.Model):
    sale_banner = models.CharField(max_length=100)
    donation_button = models.URLField(max_length=200, default='https://example.com/donate')
    body_text1 = models.CharField(max_length=100)
    body_text2 = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    lrg_banner = models.ImageField(upload_to='banners/', blank=False, null=False, default='banners/default.jpg')
    lrg_banner_2 = models.ImageField(upload_to='banners/', blank=False, null=False, default='banners/default.jpg')
    lrg_banner_3 = models.ImageField(upload_to='banners/', blank=False, null=False, default='banners/default.jpg')
    body_text1_img = models.ImageField(upload_to='banners/', blank=False, null=False, default='banners/default.jpg')
    body_text2_img = models.ImageField(upload_to='banners/', blank=False, null=False, default='banners/default.jpg')
    lrg_sponsor_img = models.ImageField(upload_to='banners/', blank=False, null=False, default='banners/default.jpg')
    sponsor_01_img = models.ImageField(upload_to='banners/', blank=False, null=False, default='banners/default.jpg')
    sponsor_02_img = models.ImageField(upload_to='banners/', blank=False, null=False, default='banners/default.jpg')
    sponsor_03_img = models.ImageField(upload_to='banners/', blank=False, null=False, default='banners/default.jpg')
    sponsor_04_img = models.ImageField(upload_to='banners/', blank=False, null=False, default='banners/default.jpg')
    sponsor_05_img = models.ImageField(upload_to='banners/', blank=False, null=False, default='banners/default.jpg')
    sponsor_06_img = models.ImageField(upload_to='banners/', blank=False, null=False, default='banners/default.jpg')
    sponsor_07_img = models.ImageField(upload_to='banners/', blank=False, null=False, default='banners/default.jpg')

class AboutPage(models.Model):
    body_text1 = models.TextField()
    body_text2 = models.TextField(default='Hello')


class PetProfile(models.Model):
    CATEGORY_CHOICES = [
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('bird', 'Bird'),
    ]
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50, default='Sparky Needs A Title')
    description = models.CharField(max_length=100)
    located = models.CharField(max_length=50)
    pet_prof_img = models.ImageField(upload_to='ppi/', blank=False, null=False, default='ppi/pet_default.jpg')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='other')

    def __str__(self):
        return f"{self.name} (ID: {self.id}) ({self.get_category_display()})"


class PrivacyPage(models.Model):
    privacy_text = models.TextField()


class TermsPage(models.Model):
    terms_text = models.TextField()
    
    