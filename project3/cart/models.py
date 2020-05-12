from django.db import models
from django.conf import settings
from products.models import Product
from django.db.models.signals import pre_save, m2m_changed

User=settings.AUTH_USER_MODEL

# Create your models here.

class CartManager(models.Manager):


    def get_or_create(self,request):
        cart_id=request.session.get('cart_id', None)
        if cart_id is None:
            cart_obj=self.new(user=request.user)
            new_obj=True
            request.session['cart_id']=cart_obj.id
            cart_id=request.session.get('cart_id')
        else:
            qs=self.get_queryset().filter(id=cart_id)
            if qs.count()==1:
                new_obj=False
                cart_obj=qs.first()
                if request.user.is_authenticated and cart_obj.user is None:
                    cart_obj.user=request.user
                    cart_obj.save()
        return cart_obj, new_obj


    def new(self,user=None):
        user_obj=None
        if user is not None:
            if user.is_authenticated:
                user_obj=user
        return self.model.objects.create(user=user_obj)



class Cart(models.Model):
    user=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    products=models.ManyToManyField(Product, blank=True)
    total=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    timestamp=models.DateTimeField(auto_now_add=True)
    objects=CartManager()

    def __str__(self):
        return str(self.id)

def m2m_changed_cart_receiver(sender,instance,action,*args,**kwargs):
    if action=='post_add' or action=='post_clear' or action=='post_remove':
        products=instance.products.all()
        total=0
        for item in products:
            total+=item.price
        instance.total=total
        instance.save()

m2m_changed.connect(m2m_changed_cart_receiver,sender=Cart.products.through)
