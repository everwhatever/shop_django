from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse

from project3.utils import unique_slug_generator
# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=166)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    slug=models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products:product_detail_view',kwargs={'slug':self.slug})


def pre_save_slug_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)

pre_save.connect(pre_save_slug_receiver,sender=Product)
