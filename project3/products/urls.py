from django.urls import path
from .views import (
    ProductUpdateView,
    ProductListView,
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
)

app_name='products'

urlpatterns=[
    path('',ProductListView.as_view(),name='product_list_view'),
    path('create/',ProductCreateView.as_view(),name='product_create_view'),
    path('update/<slug>',ProductUpdateView.as_view(),name='product_update_view'),
    path('delete/<slug>',ProductDeleteView.as_view(),name='product_delete_view'),
    path('detail/<slug>',ProductDetailView.as_view(),name='product_detail_view'),
]
