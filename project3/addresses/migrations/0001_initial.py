# Generated by Django 3.0.2 on 2020-04-04 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line', models.CharField(max_length=255)),
                ('address_type', models.CharField(choices=[('shipping', 'Shipping'), ('billing', 'Billing')], max_length=166)),
                ('city', models.CharField(max_length=166)),
                ('postal_code', models.CharField(max_length=166)),
                ('billing_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.BillingProfile')),
            ],
        ),
    ]