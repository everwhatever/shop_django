from django.shortcuts import render,redirect
from .models import Cart
from products.models import Product
from orders.models import Order
from billing.models import BillingProfile
from accounts.forms import LoginForm,GuestForm
from accounts.models import GuestEmail
from addresses.forms import AddressForm
from addresses.models import Address
# Create your views here.
def cart_home(request):
    cart_obj, new_obj=Cart.objects.get_or_create(request)
    return render(request,'cart/home.html',{'cart':cart_obj})

def cart_update(request):
    product_id=request.POST.get('product_id')
    if product_id is not None:
        cart_obj, new_obj=Cart.objects.get_or_create(request)
        product_obj=Product.objects.get(id=product_id)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
    return redirect('cart:home')



def checkout_home(request):
    cart_obj, created=Cart.objects.get_or_create(request)
    order_obj=None
    if created or cart_obj.products.count()==0:
        return redirect('cart:home')

    guest_form=GuestForm()
    login_form=LoginForm()
    address_form=AddressForm()
    billing_address_form=AddressForm()
    billing_address_id=request.session.get('billing_address_id',None)
    shipping_address_id=request.session.get('shipping_address_id',None)
    billing_profile,billing_profile_created=BillingProfile.objects.new_or_get(request)
    address_qs=None
    if billing_profile is not None:
        if request.user.is_authenticated:
            address_qs=Address.objects.filter(billing_profile=billing_profile)
        order_obj,created=Order.objects.new_or_get(billing_profile,cart_obj)
        if shipping_address_id:
            order_obj.shipping_address=Address.objects.get(id=shipping_address_id)
            del request.session['shipping_address_id']
        if billing_address_id:
            order_obj.billing_address = Address.objects.get(id=billing_address_id)
            del request.session["billing_address_id"]
        if billing_address_id or shipping_address_id:
            order_obj.save()


    if request.method=='POST':
        is_done=order_obj.check_done()
        if is_done:
            order_obj.mark_paid()
            del request.session['cart_id']
            return redirect('cart:success')




    context={
    'object':order_obj,
    'billing_profile':billing_profile,
    'login_form':login_form,
    'guest_form':guest_form,
    'address_form':address_form,
    'billing_address_form':billing_address_form,
    'address_qs':address_qs
    }

    return render(request,'cart/checkout.html',context)



def checkout_done_view(request):
    return render(request,'cart/checkout_done.html')
