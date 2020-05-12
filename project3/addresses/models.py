from django.db import models
from billing.models import BillingProfile
# Create your models here.

ADDRESSES_CHOICES=(
    ('shipping','Shipping'),
    ('billing','Billing'),
)
class Address(models.Model):
    billing_profile=models.ForeignKey(BillingProfile,on_delete=models.CASCADE)
    address_line=models.CharField(max_length=255)
    address_type=models.CharField(max_length=166,choices=ADDRESSES_CHOICES)
    city=models.CharField(max_length=166)
    postal_code=models.CharField(max_length=166)


    def __str__(self):
        return str(self.billing_profile)

    def get_address(self):
        return f"{self.address_line}\n {self.postal_code} {self.city}"
