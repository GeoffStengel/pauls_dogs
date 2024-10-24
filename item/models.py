from django.contrib.auth.models import User
from django.db import models
from django.templatetags.static import static

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=50)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name= models.CharField(max_length=50)
    description = models.TextField(blank=False, null=False, max_length=250)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_profile_imgs/', blank=False, null=False, default="default.jpg")
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    


"""   
    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return static('images/default.jpg')
"""        