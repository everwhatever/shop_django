from django.shortcuts import render
from django.urls import reverse
from .models import Product
from .forms import ProductForm
from cart.models import Cart
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
# Create your views here.


class ProductListView(ListView):
    queryset=Product.objects.all()
    template_name='products/product_list.html'

class ProductDetailView(DetailView):
    queryset=Product.objects.all()
    template_name='products/product_detail.html'

    def get_context_data(self, *args,**kwargs):
        context=super(ProductDetailView,self).get_context_data(*args,**kwargs)
        cart_obj,new_obj=Cart.objects.get_or_create(self.request)
        context['cart']=cart_obj
        return context

class ProductDeleteView(DeleteView):
    queryset=Product.objects.all()
    template_name='products/product_delete.html'

    def get_success_url(self):
        return reverse('products:products_list_view')

class ProductUpdateView(UpdateView):
    queryset=Product.objects.all()
    template_name='products/create_form.html'
    form_class=ProductForm

class ProductCreateView(CreateView):
    queryset=Product.objects.all()
    template_name='products/create_form.html'
    form_class=ProductForm
