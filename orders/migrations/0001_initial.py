# Generated by Django 4.2.10 on 2025-04-27 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=32, unique=True, verbose_name='order number')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('processing', 'Processing'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled'), ('refunded', 'Refunded')], default='pending', max_length=20, verbose_name='status')),
                ('payment_status', models.CharField(choices=[('pending', 'Pending'), ('paid', 'Paid'), ('failed', 'Failed'), ('refunded', 'Refunded')], default='pending', max_length=20, verbose_name='payment status')),
                ('shipping_name', models.CharField(max_length=255, verbose_name='shipping name')),
                ('shipping_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='shipping phone')),
                ('shipping_email', models.EmailField(max_length=254, verbose_name='shipping email')),
                ('shipping_address', models.CharField(max_length=255, verbose_name='shipping address')),
                ('shipping_address2', models.CharField(blank=True, max_length=255, verbose_name='shipping address 2')),
                ('shipping_city', models.CharField(max_length=100, verbose_name='shipping city')),
                ('shipping_state', models.CharField(max_length=100, verbose_name='shipping state')),
                ('shipping_country', django_countries.fields.CountryField(max_length=2, verbose_name='shipping country')),
                ('shipping_postal_code', models.CharField(max_length=20, verbose_name='shipping postal code')),
                ('billing_name', models.CharField(max_length=255, verbose_name='billing name')),
                ('billing_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='billing phone')),
                ('billing_email', models.EmailField(max_length=254, verbose_name='billing email')),
                ('billing_address', models.CharField(max_length=255, verbose_name='billing address')),
                ('billing_address2', models.CharField(blank=True, max_length=255, verbose_name='billing address 2')),
                ('billing_city', models.CharField(max_length=100, verbose_name='billing city')),
                ('billing_state', models.CharField(max_length=100, verbose_name='billing state')),
                ('billing_country', django_countries.fields.CountryField(max_length=2, verbose_name='billing country')),
                ('billing_postal_code', models.CharField(max_length=20, verbose_name='billing postal code')),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='subtotal')),
                ('shipping_cost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='shipping cost')),
                ('tax', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='tax')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='total')),
                ('shipping_method', models.CharField(max_length=100, verbose_name='shipping method')),
                ('tracking_number', models.CharField(blank=True, max_length=100, verbose_name='tracking number')),
                ('estimated_delivery', models.DateField(blank=True, null=True, verbose_name='estimated delivery')),
                ('payment_method', models.CharField(max_length=100, verbose_name='payment method')),
                ('transaction_id', models.CharField(blank=True, max_length=100, verbose_name='transaction ID')),
                ('payment_details', models.JSONField(blank=True, null=True, verbose_name='payment details')),
                ('customer_notes', models.TextField(blank=True, verbose_name='customer notes')),
                ('staff_notes', models.TextField(blank=True, verbose_name='staff notes')),
                ('metadata', models.JSONField(blank=True, null=True, verbose_name='metadata')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('paid_at', models.DateTimeField(blank=True, null=True, verbose_name='paid at')),
                ('shipped_at', models.DateTimeField(blank=True, null=True, verbose_name='shipped at')),
                ('delivered_at', models.DateTimeField(blank=True, null=True, verbose_name='delivered at')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('completed', 'Completed')], default='pending', max_length=20, verbose_name='status')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='amount')),
                ('reason', models.TextField(verbose_name='reason')),
                ('notes', models.TextField(blank=True, verbose_name='notes')),
                ('processed_at', models.DateTimeField(blank=True, null=True, verbose_name='processed at')),
                ('transaction_id', models.CharField(blank=True, max_length=100, verbose_name='transaction ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='refunds', to='orders.order')),
                ('processed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='processed_refunds', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'refund',
                'verbose_name_plural': 'refunds',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='OrderStatusUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('processing', 'Processing'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled'), ('refunded', 'Refunded')], max_length=20, verbose_name='status')),
                ('notes', models.TextField(blank=True, verbose_name='notes')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_updates', to='orders.order')),
            ],
            options={
                'verbose_name': 'order status update',
                'verbose_name_plural': 'order status updates',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255, verbose_name='product name')),
                ('variant_name', models.CharField(blank=True, max_length=100, verbose_name='variant name')),
                ('sku', models.CharField(max_length=100, verbose_name='SKU')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='unit price')),
                ('quantity', models.PositiveIntegerField(verbose_name='quantity')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='total price')),
                ('product_data', models.JSONField(blank=True, null=True, verbose_name='product data')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product')),
                ('variant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.productvariant')),
            ],
            options={
                'verbose_name': 'order item',
                'verbose_name_plural': 'order items',
            },
        ),
        migrations.CreateModel(
            name='HistoricalOrder',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('order_number', models.CharField(db_index=True, max_length=32, verbose_name='order number')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('processing', 'Processing'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled'), ('refunded', 'Refunded')], default='pending', max_length=20, verbose_name='status')),
                ('payment_status', models.CharField(choices=[('pending', 'Pending'), ('paid', 'Paid'), ('failed', 'Failed'), ('refunded', 'Refunded')], default='pending', max_length=20, verbose_name='payment status')),
                ('shipping_name', models.CharField(max_length=255, verbose_name='shipping name')),
                ('shipping_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='shipping phone')),
                ('shipping_email', models.EmailField(max_length=254, verbose_name='shipping email')),
                ('shipping_address', models.CharField(max_length=255, verbose_name='shipping address')),
                ('shipping_address2', models.CharField(blank=True, max_length=255, verbose_name='shipping address 2')),
                ('shipping_city', models.CharField(max_length=100, verbose_name='shipping city')),
                ('shipping_state', models.CharField(max_length=100, verbose_name='shipping state')),
                ('shipping_country', django_countries.fields.CountryField(max_length=2, verbose_name='shipping country')),
                ('shipping_postal_code', models.CharField(max_length=20, verbose_name='shipping postal code')),
                ('billing_name', models.CharField(max_length=255, verbose_name='billing name')),
                ('billing_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='billing phone')),
                ('billing_email', models.EmailField(max_length=254, verbose_name='billing email')),
                ('billing_address', models.CharField(max_length=255, verbose_name='billing address')),
                ('billing_address2', models.CharField(blank=True, max_length=255, verbose_name='billing address 2')),
                ('billing_city', models.CharField(max_length=100, verbose_name='billing city')),
                ('billing_state', models.CharField(max_length=100, verbose_name='billing state')),
                ('billing_country', django_countries.fields.CountryField(max_length=2, verbose_name='billing country')),
                ('billing_postal_code', models.CharField(max_length=20, verbose_name='billing postal code')),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='subtotal')),
                ('shipping_cost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='shipping cost')),
                ('tax', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='tax')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='total')),
                ('shipping_method', models.CharField(max_length=100, verbose_name='shipping method')),
                ('tracking_number', models.CharField(blank=True, max_length=100, verbose_name='tracking number')),
                ('estimated_delivery', models.DateField(blank=True, null=True, verbose_name='estimated delivery')),
                ('payment_method', models.CharField(max_length=100, verbose_name='payment method')),
                ('transaction_id', models.CharField(blank=True, max_length=100, verbose_name='transaction ID')),
                ('payment_details', models.JSONField(blank=True, null=True, verbose_name='payment details')),
                ('customer_notes', models.TextField(blank=True, verbose_name='customer notes')),
                ('staff_notes', models.TextField(blank=True, verbose_name='staff notes')),
                ('metadata', models.JSONField(blank=True, null=True, verbose_name='metadata')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='created at')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, verbose_name='updated at')),
                ('paid_at', models.DateTimeField(blank=True, null=True, verbose_name='paid at')),
                ('shipped_at', models.DateTimeField(blank=True, null=True, verbose_name='shipped at')),
                ('delivered_at', models.DateTimeField(blank=True, null=True, verbose_name='delivered at')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical order',
                'verbose_name_plural': 'historical orders',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
